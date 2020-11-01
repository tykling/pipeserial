PipeSerial Usage
================

Until I get something better written here are the argparse usage instructions::

   usage: pipeserial [-h] [-c [EXPECTCOUNT]] [-d] [-e EXPECT]
                     [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-p PAYLOAD]
                     [-q] [-s [SENDDELAY]] [-t [TIMEOUT]] [-v]
                     [--bytesize {5,6,7,8}] [--parity {N,E,O,S,M}]
                     [--stopbits {1,1.5,2}] [--rtscts] [--xonxoff] [--rts RTS]
                     [--dtr DTR]
                     serialport [baudrate]

   PipeSerial version 0.3.0-dev. Sends input to a serial device, awaits (expects)
   some text, and returns the output. See the manpage or ReadTheDocs for more
   info.

   positional arguments:
     serialport            Serial port device
     baudrate              Set baud rate, default: 115200

   optional arguments:
     -h, --help            show this help message and exit
     -c [EXPECTCOUNT], --count [EXPECTCOUNT]
                           Collect output from the serial device until this many
                           regex matches, default: 1
     -d, --debug           Debug mode. Equal to setting --log-level=DEBUG.
     -e EXPECT, --expect EXPECT
                           Regular expressions to expect as end of the output.
                           Can be specified multiple times, default: [' OK ', '
                           ERROR ']
     -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                           Logging level. One of DEBUG, INFO, WARNING, ERROR,
                           CRITICAL. Defaults to INFO.
     -p PAYLOAD, --payload PAYLOAD
                           The payload to send to the serial device, instead of
                           getting it from standard input. Default None.
     -q, --quiet           Quiet mode. No output at all if no errors are
                           encountered. Equal to setting --log-level=WARNING.
     -s [SENDDELAY], --send-delay [SENDDELAY]
                           Delay in seconds between sending each line of payload
                           to the serial device, default: 0.9
     -t [TIMEOUT], --timeout [TIMEOUT]
                           Timeout in seconds before giving up waiting for the
                           expected output, default: 30
     -v, --version         Show PipeSerial version and exit.

   Serial port options:
     --bytesize {5,6,7,8}  Set bytesize, one of {5 6 7 8}, default: 8
     --parity {N,E,O,S,M}  Set parity, one of {N E O S M}, default: N
     --stopbits {1,1.5,2}  Set stopbits, one of {1 1.5 2}, default: 1
     --rtscts              Enable RTS/CTS hardware flow control, default: off
     --xonxoff             Enable software flow control, default: off
     --rts RTS             Set initial RTS line state, one of {0, 1}, default:
                           none
     --dtr DTR             Set initial DTR line state, one of {0, 1}, default:
                           none

Read on for examples.
