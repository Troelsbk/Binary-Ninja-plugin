from mips_plugin_external_functions import make_tokens
from mips_instructions import branchInstructions
from binascii import hexlify
import logging
import ctypes
import binaryninja
from mips_parser import m_parser
from binaryninja import (
Architecture,
log_info, 
InstructionInfo,
log_error,
BranchType,
InstructionTextTokenType,
InstructionTextToken)


class Custom_MipsPlugin(Architecture):
    name= "Custom_MipsPlugin"
    stack_pointer = 'sp'

    def get_instruction_info(self, data, addr):
        """implement branches in binaryninja"""

        #parse instruction info from mips_parser module
        instruction = m_parser(data[:4])
        instruction_name = instruction.name
        logging.debug("[get_instruction_info]: %s:instruction_name: %s" % (hex(addr), instruction_name))
        out = InstructionInfo()
        out.length = 4
        
        #is next instruction nop
        is_next_nop = lambda : bool(m_parser(data[4:8]).name == 'nop') 

        if instruction_name == "jr":
            out.add_branch(BranchType.FunctionReturn)

        elif instruction_name == "bal":# or instruction_name == "jal":
            assert instruction.type == 'I', 'Wrong instruction_type'
            immediate = instruction.parse.get('immediate', None)
            c_type_immediate_value = ctypes.c_short(immediate).value
            c_type_immediate_value_extended = c_type_immediate_value << 2
            out.add_branch(BranchType.CallDestination, addr + 4 + c_type_immediate_value_extended)

        #not implemented
        #elif instruction_name == "jmp":
        #    out.add_branch(BranchType.UnconditionalBranch, src_operand_value)

        elif instruction_name in branchInstructions:
            assert instruction.type == 'I', 'Wrong instruction_type'
            if is_next_nop():
                out.length = 4  #changed from 8
            immediate = instruction.parse.get('immediate', None)
            c_type_immediate_value = ctypes.c_short(immediate).value
            c_type_immediate_value_extended = c_type_immediate_value << 2
            out.add_branch(BranchType.TrueBranch, c_type_immediate_value_extended + addr + 4)
            out.add_branch(BranchType.FalseBranch, addr + 4)
        
        return out

    def perform_get_instruction_low_level_il(self, data, addr, il):
        return None

    def get_instruction_text(self, data, addr):
        """implement instruction text part in binaryninja: address, opcode, instruction"""
        tokens, length = make_tokens(data, addr)

        return tokens, length




Custom_MipsPlugin.register()
