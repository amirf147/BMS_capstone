/*
  Software serial multple serial test

 Receives from the hardware serial, sends to software serial.
 Receives from software serial, sends to hardware serial.

 The circuit:
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)

 Note:
 Not all pins on the Mega and Mega 2560 support change interrupts,
 so only the following can be used for RX:
 10, 11, 12, 13, 50, 51, 52, 53, 62, 63, 64, 65, 66, 67, 68, 69

 Not all pins on the Leonardo support change interrupts,
 so only the following can be used for RX:
 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI).

 created back in the mists of time
 modified 25 May 2012
 by Tom Igoe
 based on Mikal Hart's example
 further edits and usage by Amir Farhadi 17/04/2021
 This example code is in the public domain.

 */
#include <SoftwareSerial.h>
#include <stdint.h>


//#define SERIAL_TX_BUFFER_SIZE 256
//#define SERIAL_RX_BUFFER_SIZE 256
#define UI_BUFFER_SIZE 64
#define SERIAL_TERMINATOR '\n'

SoftwareSerial mySerial(2, 3); // RX, TX
String comdata = "";
char ui_buffer[UI_BUFFER_SIZE];
void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);

 while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  delay(200);
}

void loop() // run over and over
{
//  delay(2000);
//  mySerial.println("AT");   
//  delay(200);
//  mySerial.println("AT+BTSTATUS?");
//  delay(200);
//  mySerial.println("AT+BTGETPROF=1");
//  delay(200);
//  mySerial.println("AT+BTCONNECT=1,4");
//  delay(2000);

  int counter = 0;
  char str[30];
  int rx = 0;
  mySerial.println("AT+BTSPPSEND=5");
  delay(500);
  mySerial.listen();
  while(1)
  { 
    if (mySerial.available() > 1)
      mySerial.read();
    mySerial.println("hello");
    delay(200);
    if (mySerial.available() > 1)
      mySerial.read();
    break;
//    delay(1000);
//    counter++;
//    if (counter == 100)
//      break;
//    Serial.println(counter);

    
    
//    while(mySerial.available() > 0)
//      rx = mySerial.read();
//      Serial.write(mySerial.read());
//    while(Serial.available())
//      mySerial.write(Serial.read());  //Arduino send the sim808 feedback to computer
  }
  //Serial.println("outerloop");
  //delay(30000); 
}

uint8_t read_data()
{
  uint8_t index = 0; //index to hold current location in ui_buffer
  int c; // single character used to store incoming keystrokes
  while (index < UI_BUFFER_SIZE-1)
  {
    c = Serial.read(); //read one character
    if (((char) c == '\r') || ((char) c == '\n')) break; // if carriage return or linefeed, stop and return data
    if ( ((char) c == '\x7F') || ((char) c == '\x08') )   // remove previous character (decrement index) if Backspace/Delete key pressed      index--;
    {
      if (index > 0) index--;
    }
    else if (c >= 0)
    {
      ui_buffer[index++]=(char) c; // put character into ui_buffer
    }
  }
  ui_buffer[index]='\0';  // terminate string with NULL

  if ((char) c == '\r')    // if the last character was a carriage return, also clear linefeed if it is next character
  {
    delay(10);  // allow 10ms for linefeed to appear on serial pins
    if (Serial.peek() == '\n') Serial.read(); // if linefeed appears, read it and throw it away
  }

  return index; // return number of characters, not including null terminator
}

// Read a float value from the serial interface
float read_float()
{
  float data;
  read_data();
  data = atof(ui_buffer);
  return(data);
}

// Read an integer from the serial interface.
// The routine can recognize Hex, Decimal, Octal, or Binary
// Example:
// Hex:     0x11 (0x prefix)
// Decimal: 17
// Octal:   021 (leading zero prefix)
// Binary:  B10001 (leading B prefix)
int32_t read_int()
{
  int32_t data;
  read_data();
  if (ui_buffer[0] == 'm')
    return('m');
  if ((ui_buffer[0] == 'B') || (ui_buffer[0] == 'b'))
  {
    data = strtol(ui_buffer+1, NULL, 2);
  }
  else
    data = strtol(ui_buffer, NULL, 0);
  return(data);
}

// Read a string from the serial interface.  Returns a pointer to the ui_buffer.
char *read_string()
{
  read_data();
  return(ui_buffer);
}

// Read a character from the serial interface
int8_t read_char()
{
  read_data();
  return(ui_buffer[0]);
}
