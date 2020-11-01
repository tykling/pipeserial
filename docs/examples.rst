PipeSerial Examples
===================

Basic Use
---------
Basic usage is just piping the input to pipeserial, telling it which output to expect, and the serial device. In these examples the serial devices are LTE modems responding to AT commands::

   [tykling@container1 ~]$ echo "AT" | sudo pipeserial -e OK /dev/ttyU0.3
   AT
   OK
   [tykling@container1 ~]$ 

Same thing with debug enabled::

   [tykling@container1 ~]$ echo "AT" | sudo pipeserial -d -e OK /dev/ttyU0.3
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.main():311:  Initialising the PipeSerial class
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.__init__():54:  Configuring serial port {serialport} ...
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.main():329:  Payload is 3 bytes
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.main():335:  Output to expect: ['OK']
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.open():75:  Opening serial port...
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.open():82:  Serial port opened OK!
   2020-10-31 22:41:37 +0000 pipeserial DEBUG pipeserial.run():107:  Sending payload line: AT
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.run():116:  Will stop collecting after 1 matches
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.run():127:  Done! Returning 9 bytes of output from serial device
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.close():133:  Closing serial port...
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.close():135:  Serial port closed
   2020-10-31 22:41:38 +0000 pipeserial DEBUG pipeserial.main():355:  Got 3 lines of output from serial device /dev/ttyU0.3:
   AT
   OK
   [tykling@container1 ~]$ 


Expecting Output
----------------
The regex matcher in pexpect is stream / single character based so ^ and $ will not work in the expect regexes. To match the start of a line add ``\r\n`` before the string, to match the end of a line match ``\r\n`` after the string.

The default is to match ``\r\nOK\r\n`` and ``\r\nERROR\r\n`` but this can be changed with ``-e`` / ``--expect`` as seen below::

   [tykling@container1 ~]$ echo "AT" | sudo pipeserial -e OK -d /dev/ttyU0.3
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.main():311:  Initialising the PipeSerial class
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.__init__():54:  Configuring serial port {serialport} ...
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.main():329:  Payload is 3 bytes
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.main():335:  Output to expect: ['OK']
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.open():75:  Opening serial port...
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.open():82:  Serial port opened OK!
   2020-10-31 22:45:20 +0000 pipeserial DEBUG pipeserial.run():107:  Sending payload line: AT
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.run():114:  Collecting output, looking for one of these regular expressions: ['OK']
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.run():116:  Will stop collecting after 1 matches
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.run():120:  Found match: 'OK' (match number 1 of 1)
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.run():127:  Done! Returning 7 bytes of output from serial device
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.close():133:  Closing serial port...
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.close():135:  Serial port closed
   2020-10-31 22:45:21 +0000 pipeserial DEBUG pipeserial.main():355:  Got 2 lines of output from serial device /dev/ttyU0.3:
   AT
   OK
   [tykling@container1 ~]$ 

Multiple lines of output from the serial device will be returned up until the expected output is encountered::

   [tykling@container1 ~]$ echo "ATI" | sudo pipeserial /dev/ttyU0.3
   ATI
   Quectel
   EC25
   Revision: EC25EFAR06A06M4G

   OK

   [tykling@container1 ~]$

Same thing with a different LTE modem::

   [tykling@container1 ~]$ echo "ATI" | sudo pipeserial /dev/ttyU1.2
   ATI
   Manufacturer: Huawei Technologies Co., Ltd.
   Model: ME909s-120
   Revision: 11.617.15.00.00
   IMEI: 123456789012345
   +GCAP: +CGSM,+DS,+ES

   OK

   [tykling@container1 ~]$ 

Multiline Input
---------------
Multiple lines of payload can be sent to the serial device. Remember ``-e`` to make ``echo`` understand ``\n``. PipeSerial is also told with ``-c 2`` to collect output until 2 expect matches has been seen::

   [tykling@container1 ~]$ echo -ne "AT\nATI" | sudo venv/bin/python pipeserial.py -c 2 -d /dev/ttyU0.3      
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.main():311:  Initialising the PipeSerial class
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.__init__():54:  Configuring serial port {serialport} ...
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.main():329:  Payload is 6 bytes
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.main():335:  Output to expect: ['\r\nOK\r\n', '\r\nERROR\r\n']
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.open():75:  Opening serial port...
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.open():82:  Serial port opened OK!
   2020-10-31 22:49:42 +0000 pipeserial DEBUG pipeserial.run():107:  Sending payload line: AT
   2020-10-31 22:49:43 +0000 pipeserial DEBUG pipeserial.run():107:  Sending payload line: ATI
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.run():114:  Collecting output, looking for one of these regular expressions: ['\r\nOK\r\n', '\r\nERROR\r\n']
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.run():116:  Will stop collecting after 2 matches
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.run():120:  Found match: 'OK' (match number 1 of 2)
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.run():120:  Found match: 'OK' (match number 2 of 2)
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.run():127:  Done! Returning 64 bytes of output from serial device
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.close():133:  Closing serial port...
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.close():135:  Serial port closed
   2020-10-31 22:49:44 +0000 pipeserial DEBUG pipeserial.main():355:  Got 9 lines of output from serial device /dev/ttyU0.3:
   AT
   OK
   ATI
   Quectel
   EC25
   Revision: EC25EFAR06A06M4G

   OK

   [tykling@container1 ~]$ 

The output from the serial device is sent to stdout and the logging is sent to stderr.
