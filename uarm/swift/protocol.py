#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

OK = "OK"
TIMEOUT = 'TIMEOUT'

# Device Info Cmd
GET_DEVICE_TYPE = "P2201"
GET_HARDWARE_VERSION = "P2202"
GET_FIRMWARE_VERSION = "P2203"
GET_API_VERSION = "P2204"
GET_DEVICE_UNIQUE = "P2205"
GET_EEPROM = "M2211 N0 A{} T{}"

# Set Cmd
SET_POSITION = "G0 X{} Y{} Z{} F{}"
SET_POSITION_RELATIVE = "G2204 X{} Y{} Z{} F{}"
SET_SERVO_ANGLE = "G2202 N{} V{} F{}"
SET_POLAR = "G2201 S{} R{} H{} F{}"
SET_POLAR_RELATIVE = "G2205 S{} R{} H{} F{}"
SET_PUMP = "M2231 V{}"
SET_GRIPPER = "M2232 V{}"
SET_BUZZER = "M2210 F{} T{}"
SET_ATTACH_SERVO = "M2201 N{}"
SET_ATTACH_ALL_SERVO = "M17"
SET_DETACH_SERVO = "M2202 N{}"
SET_DETACH_ALL_SERVO = "M2019"
SET_MODE = "M2400 S{}"
SET_SERIAL_MODE = "M2500"
SET_EEPROM = "M2212 N0 A{} T{} V{}"
SET_BLUETOOTH = "M2234 V{}"
SET_HEIGHT_OFFSET = "M2410 S{}"
SET_DEFAULT_ACC = "M204 P{} T{} R{}"
SET_MAX_JERK = "M205 X{} Z{} E{}"
SET_TEMPERATURE_BLOCK = "M109 S{}"  # block but will auto report temperature
SET_TEMPERATURE_UNBLOCK = "M104 S{}"  # unblock but not auto report temperature
OPEN_FAN = "M106"
CLOSE_FAN = "M107"
SET_ACC = "M204 A{}"

# Get Cmd
GET_PUMP = "P2231"
GET_POSITION = "P2220"
GET_SERVO_ANGLE = "P2200"
GET_LIMIT_SWITCH = "P2233"
GET_POLAR = "P2221"
GET_GRIPPER = "P2232"
GET_ANALOG = "P2241 N{}"
GET_DIGITAL = "P2240 N{}"
GET_MODE = "P2400"
GET_SERVO_ATTACH = "M2203 N{}"
GET_POWER_STATUS = "P2234"
GET_IS_MOVE = "M2200"

# Report Cmd
SET_REPORT_POSITION = "M2120 V{}"
SET_REPORT_KEYS = "M2213 V{}"

# Report Prefix
REPORT_POSITION_PREFIX = "@3"
REPORT_KEYS_PREFIX = "@4"  # @4 B0 V1
REPORT_POWER_PREFIX = "@5"          # @5 V1 ==> on
REPORT_LIMIT_SWITCH_PREFIX = "@6"    # @6 N0 V1 ==> on,  @6 N0 V0 ==> off
REPORT_STOP_MOVE_PREFIX = "@9"


# Grove
SET_GROVE_INIT = "M2305 P{} N{}"
SET_GROVE_RELEASE = "M2304 P{}"
SET_GROVE_CONTROL = "M2307 P{} V{}"
SET_GROVE_REPORT = "M2306 P{} V{}"
REPORT_GROVE_PREFIX = "@11"  # @10 N10  "@11"


SERVO_BOTTOM = 0
SERVO_LEFT = 1
SERVO_RIGHT = 2
SERVO_HAND = 3

EEPROM_DATA_TYPE_BYTE = 1
EEPROM_DATA_TYPE_INTEGER = 2
EEPROM_DATA_TYPE_FLOAT = 4

