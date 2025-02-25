""" Describe PRC interface for the Emulator """

from devsure.rpc.rpc_to_emulator import RpcToEmulator, rpc_class, rpc_local, rpc_remote
from typing import Annotated

__all__= [
    'EmulatorRpc'
]


@rpc_class
class EmulatorRpc(RpcToEmulator):
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
