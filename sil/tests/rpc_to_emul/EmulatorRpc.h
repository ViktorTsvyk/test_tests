/**
 * @file EmulatorRpc.h
 * 
 * This file is normally generated by Python (devsure/rpc).
 * It contains the C/C++ API declarations for the RPC.
 * Generated from the Python class EmulatorRpc.
 * Located in devsure/devsure/rpc/test/rpc_to_emul/emulator_rpc.py.
 */

#ifndef EMULATORRPC_H
#define EMULATORRPC_H

//Common types used in communication (access to (c)stdint(.h) types)
#include "Emulator/RPC/TypesRPC.h"


#ifdef  __cplusplus
//C++ part of the generated code
//actual setup starts here (NOTE: generated C API are below)

#include "Emulator/RPC/InterfaceRPC.h"
#include <memory>

/// Setup actual RPC communication (called by Emulator startup code)
void SetupRPC_EmulatorRpc(
    const std::shared_ptr<InterfaceChannelRPC>& ccalls_fwaits_toUse,
    const std::shared_ptr<InterfaceChannelRPC>& cwaits_fcalls_toUse,
    bool runAsynchronously = false
);

extern "C"{
#endif //__cplusplus
            
// __________________________________________________________________________
// Structures

// __________________________________________________________________________
// Test Platform (framework) API called from C
void framework_api1();
int8_t framework_api2(char c);
uint8_t framework_api3();
int16_t framework_api4(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16);
uint16_t framework_api5();
int32_t framework_api6(uint8_t u8, int16_t i16, int32_t i32, uint32_t u32);
uint32_t framework_api7();
int64_t framework_api8(int16_t i16, int32_t i32, int64_t i64, uint32_t u32);
uint64_t framework_api9();
float framework_api10(int64_t i64, uint64_t u64, float f);
double framework_api11();
void framework_api12(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16, int32_t i32, uint32_t u32, int64_t i64, uint64_t u64, float f, double d, char s1[7]);

// __________________________________________________________________________
// API to be implemented in C (that is called from the framework)
// CALLED BY OTHER SIDE (Python), USER SHALL IMPLEMENT THESE HERE IN C/C++
void cpp_api1();
int8_t cpp_api2(char c);
uint8_t cpp_api3();
int16_t cpp_api4(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16);
uint16_t cpp_api5();
int32_t cpp_api6(uint8_t u8, int16_t i16, int32_t i32, uint32_t u32);
uint32_t cpp_api7();
int64_t cpp_api8(int16_t i16, int32_t i32, int64_t i64, uint32_t u32);
uint64_t cpp_api9();
float cpp_api10(int64_t i64, uint64_t u64, float f);
double cpp_api11();
void cpp_api12(char c, int8_t i8, uint8_t u8, int16_t i16, uint16_t u16, int32_t i32, uint32_t u32, int64_t i64, uint64_t u64, float f, double d, char s1[7]);

#ifdef __cplusplus

// __________________________________________________________________________
// serialization

// __________________________________________________________________________
// deserialization

} // extern "C"

#endif // __cplusplus
#endif // EMULATORRPC_H 
