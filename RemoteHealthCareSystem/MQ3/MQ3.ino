
const int AOUTpin=0;//the AOUT pin of the alcohol sensor goes into analog pin A0 of the arduino
float value;
float val;
void setup() {
Serial.begin(9600);//sets the baud rate
pinMode(AOUTpin, OUTPUT);//sets the pin as an input to the arduino
}

void loop()
{
value= analogRead(AOUTpin);//reads the analaog value from the alcohol sensor's AOUT pin
val=(5/1023.0)*value;
Serial.println(val);//prints the alcohol value
delay(100);

}
