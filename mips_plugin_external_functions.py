from ctypes import c_short
from mips_instructions import *
from mips_parser import *
from binaryninja import InstructionTextTokenType, InstructionTextToken
from binaryninja import log_info, log_error

def make_tokens(data, addr):
    mipsIns = m_parser(data[:4])
    instruction_name = mipsIns.name

    instruction_type = mipsIns.type
    instruction_length = 4

    #is_next_nop = lambda : bool(m_parser(data[4:8]).name == 'nop') 
    #if instruction_name in branchInstructions and is_next_nop():
    #    instruction_length = 8

    tokens = [InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, '{<:7}')]
    tokens = [InstructionTextToken(InstructionTextTokenType.InstructionToken, '{:7s}'.format(instruction_name))]


    if instruction_type == 'R':
        rs = mipsIns.parse['rs']
        rd = mipsIns.parse['rd']
        rt = mipsIns.parse['rt']
        #implement pseudoinstruction move
        if instruction_name == 'or' and rt == 'zero':
            tokens = [InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, '{<:7}')]
            tokens = [InstructionTextToken(InstructionTextTokenType.InstructionToken, '{:7s}'.format('move'))]
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rd)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ',' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rs)))
        #steamline jr
        elif instruction_name == 'jr':
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rs)))
        else:
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rd)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ',' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rs)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ',' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rt)))

    elif instruction_type == 'I':
        rt = mipsIns.parse.get('rt')
        rs = mipsIns.parse.get('rs')

        if instruction_name in unsigned_instructions:
            immediate = mipsIns.parse.get('immediate')
        else:
            #using c_types.c_short to get signed 16 bit value
            immediate = c_short(mipsIns.parse.get('immediate')).value

        if instruction_name in load_store_ins or instruction_name == 'lui':
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rt)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ',' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.IntegerToken, hex(immediate), immediate))
            tokens.append(InstructionTextToken(InstructionTextTokenType.TextToken, '(' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rs)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.TextToken, ')' ))
        #elif instruction_name == 'bal' or instruction_name == 'beq':
        elif instruction_name in branchInstructions:
            immediate = (c_short(mipsIns.parse.get('immediate')).value << 2) + 4
            immediate += addr
            tokens.append(InstructionTextToken(InstructionTextTokenType.PossibleAddressToken, hex(immediate), immediate))
        else:
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rt)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ',' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.RegisterToken, '${}'.format(rs)))
            tokens.append(InstructionTextToken(InstructionTextTokenType.OperandSeparatorToken, ',' ))
            tokens.append(InstructionTextToken(InstructionTextTokenType.IntegerToken, hex(immediate), immediate))
    elif instruction_type == 'J':
        pass

    return tokens, instruction_length
    
if __name__ == '__main__':
    with open("/home/troels/scripts/mips_plugin/main.bin", 'rb') as main_bin:
        addr = 0x00400908
        main_bin.seek(addr)
        raw_main_data = main_bin.read()
        raw_main_data_chunck = [raw_main_data[index:index+4] for index in range(0, len(raw_main_data), 4)]
        for chunck in raw_main_data_chunck:
            token, length = make_tokens(chunck, addr)
            print(token)
            addr += length
