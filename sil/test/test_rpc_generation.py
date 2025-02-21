""" Basic tests for the rpc proxy and stubs generation module.
"""

import os
import unittest
from typing import Annotated

from devsure.rpc.serialization import serializable
from devsure.rpc.rpc import rpc_class, rpc_local, rpc_remote
from devsure.rpc.rpc_connection import RpcSupport


@serializable
class FrameworkAPIStructureDemo:
    """ Structure to be used in API calls """
    c: Annotated[bytes, 'char']
    i8: Annotated[int, 'int8_t']
    u8: Annotated[int, 'uint8_t']
    i16: Annotated[int, 'int16_t']
    u16: Annotated[int, 'uint16_t']
    i32: Annotated[int, 'int32_t']
    u32: Annotated[int, 'uint32_t']
    i64: Annotated[int, 'int64_t']
    u64: Annotated[int, 'uint64_t']
    f: Annotated[float, 'float']
    d: Annotated[float, 'double']
    s1: Annotated[bytes, 'char', 7]
    # s2: Annotated[bytes, 'uint8_t', 7]


@serializable
class CppAPIStructureDemo:
    """ Structure to be used in API calls """
    c: Annotated[bytes, 'char']
    i8: Annotated[int, 'int8_t']
    u8: Annotated[int, 'uint8_t']
    i16: Annotated[int, 'int16_t']
    u16: Annotated[int, 'uint16_t']
    i32: Annotated[int, 'int32_t']
    u32: Annotated[int, 'uint32_t']
    i64: Annotated[int, 'int64_t']
    u64: Annotated[int, 'uint64_t']
    f: Annotated[float, 'float']
    d: Annotated[float, 'double']
    s1: Annotated[bytes, 'char', 7]
    # s2: Annotated[bytes, 'uint8_t', 7]


@rpc_class
class SampleGenerated(RpcSupport):
    """ Sample class to be generated as RPC API """

    @rpc_local
    def framework_api1(self):
        """ Method that will be called from the other side """
        pass

    @rpc_local
    def framework_api2(self, c: Annotated[bytes, 'char']) -> Annotated[int, 'int8_t']:
        """ Method that will be called from the other side """
        return c[0] + 1
    
    @rpc_local
    def framework_api3(self) -> Annotated[int, 'uint8_t']:
        """ Method that will be called from the other side """
        return 1
    
    @rpc_local
    def framework_api4(self, c: Annotated[bytes, 'char'], i8: Annotated[int, 'int8_t'], u8: Annotated[int, 'uint8_t'], i16: Annotated[int, 'int16_t'], u16: Annotated[int, 'uint16_t']) -> Annotated[int, 'int16_t']:
        """ Method that will be called from the other side """
        return c + i8 + u8 + i16 + u16
    
    @rpc_local
    def framework_api5(self) -> Annotated[int, 'uint16_t']:
        return 5
    
    @rpc_local
    def framework_api6(self, u8: Annotated[int, 'uint8_t'], i16: Annotated[int, 'int16_t'], i32: Annotated[int, 'int32_t'], u32: Annotated[int, 'uint32_t']) -> Annotated[int, 'int32_t']:
        """ Method that will be called from the other side """
        return u8 + i16 + i32 + u32
    
    @rpc_local
    def framework_api7(self) -> Annotated[int, 'uint32_t']:
        """ Method that will be called from the other side """
        return 7
    
    @rpc_local
    def framework_api8(self, i16: Annotated[int, 'int16_t'], i32: Annotated[int, 'int32_t'], i64: Annotated[int, 'int64_t'], u32: Annotated[int, 'uint32_t']) -> Annotated[int, 'int64_t']:
        """ Method that will be called from the other side """
        return i16 + i32 + i64 + u32
    
    @rpc_local
    def framework_api9(self) -> Annotated[int, 'uint64_t']:
        """ Method that will be called from the other side """
        return 9
    
    @rpc_local
    def framework_api10(self, i64: Annotated[int, 'int64_t'], u64: Annotated[int, 'uint64_t'], f: Annotated[float, 'float']) -> Annotated[float, 'float']:
        """ Method that will be called from the other side """
        return i64 + u64 + f
    
    @rpc_local
    def framework_api11(self) -> Annotated[float, 'double']:
        """ Method that will be called from the other side """
        return 11
    
    @rpc_local
    def framework_api12(self, c: Annotated[bytes, 'char'], i8: Annotated[int, 'int8_t'], u8: Annotated[int, 'uint8_t'], i16: Annotated[int, 'int16_t'], u16: Annotated[int, 'uint16_t'], i32: Annotated[int, 'int32_t'], u32: Annotated[int, 'uint32_t'], i64: Annotated[int, 'int64_t'], u64: Annotated[int, 'uint64_t'], f: Annotated[float, 'float'], d: Annotated[float, 'double'], s1: Annotated[bytes, 'char', 7]) -> None:
        pass

    # TODO: other rpc_local with structures

    @rpc_remote
    def cpp_api1(self):
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api2(self, c: Annotated[bytes, 'char']) -> Annotated[int, 'int8_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api3(self) -> Annotated[int, 'uint8_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api4(self, c: Annotated[bytes, 'char'], i8: Annotated[int, 'int8_t'], u8: Annotated[int, 'uint8_t'], i16: Annotated[int, 'int16_t'], u16: Annotated[int, 'uint16_t']) -> Annotated[int, 'int16_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api5(self) -> Annotated[int, 'uint16_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api6(self, u8: Annotated[int, 'uint8_t'], i16: Annotated[int, 'int16_t'], i32: Annotated[int, 'int32_t'], u32: Annotated[int, 'uint32_t']) -> Annotated[int, 'int32_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api7(self) -> Annotated[int, 'uint32_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api8(self, i16: Annotated[int, 'int16_t'], i32: Annotated[int, 'int32_t'], i64: Annotated[int, 'int64_t'], u32: Annotated[int, 'uint32_t']) -> Annotated[int, 'int64_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api9(self) -> Annotated[int, 'uint64_t']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api10(self, i64: Annotated[int, 'int64_t'], u64: Annotated[int, 'uint64_t'], f: Annotated[float, 'float']) -> Annotated[float, 'float']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api11(self) -> Annotated[float, 'double']:
        """ Method that we call on the other side """

    @rpc_remote
    def cpp_api12(self, c: Annotated[bytes, 'char'], i8: Annotated[int, 'int8_t'], u8: Annotated[int, 'uint8_t'], i16: Annotated[int, 'int16_t'], u16: Annotated[int, 'uint16_t'], i32: Annotated[int, 'int32_t'], u32: Annotated[int, 'uint32_t'], i64: Annotated[int, 'int64_t'], u64: Annotated[int, 'uint64_t'], f: Annotated[float, 'float'], d: Annotated[float, 'double'], s1: Annotated[bytes, 'char', 7]) -> None:
        pass


class TestRPCGeneration(unittest.TestCase):
    """ Test RPC generation """

    def test_rpc_generation_header(self):
        """ Test generation of RPC API in the header file """
        # verify that the file named SampleGenerated.h is present
        # in the same folder as the folder of the current module

        # Get the directory of the current module
        current_module_dir = os.path.dirname(__file__)
        # Construct the full path to the file
        file_path = os.path.join(current_module_dir, 'SampleGenerated.h')
        
        # Check if the file exists
        self.assertTrue(os.path.isfile(file_path), f"File {file_path} does not exist")

        # Read the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Check if the file contains the expected content
        self.assertIn("void framework_api1()", content)
        self.assertIn("int8_t framework_api2(char c)", content)
        self.assertIn("uint8_t framework_api3()", content)
        self.assertIn("int16_t framework_api4(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16)", content)
        self.assertIn("uint16_t framework_api5()", content)
        self.assertIn("int32_t framework_api6(uint8_t u8, int16_t i16, int32_t i32, uint32_t u32)", content)
        self.assertIn("uint32_t framework_api7()", content)
        self.assertIn("int64_t framework_api8(int16_t i16, int32_t i32, int64_t i64, uint32_t u32)", content)
        self.assertIn("uint64_t framework_api9()", content)
        self.assertIn("float framework_api10(int64_t i64, uint64_t u64, float f)", content)
        self.assertIn("double framework_api11()", content)
        self.assertIn("void framework_api12(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16, int32_t i32, uint32_t u32, int64_t i64, uint64_t u64, float f, double d, char s1[7])", content)
        
        # API to be implemented in the C++ side must also be present
        self.assertIn("void cpp_api1()", content)
        self.assertIn("int8_t cpp_api2(char c)", content)
        self.assertIn("uint8_t cpp_api3()", content)
        self.assertIn("int16_t cpp_api4(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16)", content)
        self.assertIn("uint16_t cpp_api5()", content)
        self.assertIn("int32_t cpp_api6(uint8_t u8, int16_t i16, int32_t i32, uint32_t u32)", content)
        self.assertIn("uint32_t cpp_api7()", content)
        self.assertIn("int64_t cpp_api8(int16_t i16, int32_t i32, int64_t i64, uint32_t u32)", content)
        self.assertIn("uint64_t cpp_api9()", content)
        self.assertIn("float cpp_api10(int64_t i64, uint64_t u64, float f)", content)
        self.assertIn("double cpp_api11()", content)
        self.assertIn("void cpp_api12(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16, int32_t i32, uint32_t u32, int64_t i64, uint64_t u64, float f, double d, char s1[7])", content)

    def test_rpc_generation_cpp(self):
        """ Test generation of RPC API in the source file """
        # verify that the file named SampleGenerated.cpp is present
        # in the same folder as the folder of the current module

        # Get the directory of the current module
        current_module_dir = os.path.dirname(__file__)
        # Construct the full path to the file
        file_path = os.path.join(current_module_dir, 'SampleGenerated.cpp')

        # Check if the file exists
        self.assertTrue(os.path.isfile(file_path), f"File {file_path} does not exist")

        # Read the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Check if the file contains the expected content
        self.assertIn("void framework_api1()", content)
        self.assertIn("int8_t framework_api2(char c)", content)
        self.assertIn("uint8_t framework_api3()", content)
        self.assertIn("int16_t framework_api4(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16)", content)
        self.assertIn("uint16_t framework_api5()", content)
        self.assertIn("int32_t framework_api6(uint8_t u8, int16_t i16, int32_t i32, uint32_t u32)", content)
        self.assertIn("uint32_t framework_api7()", content)
        self.assertIn("int64_t framework_api8(int16_t i16, int32_t i32, int64_t i64, uint32_t u32)", content)
        self.assertIn("uint64_t framework_api9()", content)
        self.assertIn("float framework_api10(int64_t i64, uint64_t u64, float f)", content)
        self.assertIn("double framework_api11()", content)
        self.assertIn("void framework_api12(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16, int32_t i32, uint32_t u32, int64_t i64, uint64_t u64, float f, double d, char s1[7])", content)
        
        # API to be implemented in the C++ must be invoked!
        self.assertIn("cpp_api1()", content)
        self.assertIn("= cpp_api2(c)", content)
        self.assertIn("= cpp_api3()", content)
        self.assertIn("= cpp_api4(c, i8, u8, i16, u16)", content)
        self.assertIn("= cpp_api5()", content)
        self.assertIn("= cpp_api6(u8, i16, i32, u32)", content)
        self.assertIn("= cpp_api7()", content)
        self.assertIn("= cpp_api8(i16, i32, i64, u32)", content)
        self.assertIn("= cpp_api9()", content)
        self.assertIn("= cpp_api10(i64, u64, f)", content)
        self.assertIn("= cpp_api11()", content)
        self.assertIn("cpp_api12(c, i8, u8, i16, u16, i32, u32, i64, u64, f, d, s1)", content)


# Example usage
if __name__ == '__main__':
    unittest.main()



        
