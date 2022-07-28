unsigned long secs;

const int r_led = 8;
const int y_led = 4;

bool blinker = true;

unsigned long current;

bool set = true;
long int i = 0;
int cal_time = 10 * 1000;
long int average_mic = 0;
long int average_photo = 0;

int curr_mic;

int peaks;
unsigned long first_peak;

const int diviation_mic = 7;
const int diviation_photo = 100;

const int speed_of_sound = 343;

void setup() {
  Serial.begin(9600);
  pinMode(r_led, OUTPUT);
  pinMode(y_led, OUTPUT);
}

void loop() {

  // calibration
  while (set == true) {
    secs = millis();
    i += 1;
    average_mic += analogRead(A3);
    average_photo += analogRead(A0);

    if (secs % 500 == 0 and secs != cal_time - 500) {
      if (blinker == true) {
        digitalWrite(y_led, HIGH);
        blinker = false;
        delay(1);
      }
      else {
        digitalWrite(y_led, LOW);
        blinker = true;
        delay(1);
      }
    }
    while (cal_time - 600 <= secs and secs < cal_time) {
      secs = millis();
      digitalWrite(y_led, HIGH);
    }

    if (secs == cal_time) {
      average_mic = average_mic / i;
      average_photo = average_photo / i;

      digitalWrite(y_led, LOW);

      Serial.println(average_mic);
      Serial.println(average_photo);
      Serial.println("");

      set = false;
      break;
    }
  }

  // main code

  //  Serial.print(analogRead(A0));
  //  Serial.print(",");
  //  Serial.println(analogRead(A3));

  if (analogRead(A0) >= average_photo + diviation_photo) {
    digitalWrite(r_led, HIGH);
    Serial.println("LIGHT");
    secs = millis();
    current = secs;
    peaks = 0;
    first_peak = 0;

    while (secs - current < 10000) {
      secs = millis();
      curr_mic = analogRead(A3);

      //       Serial.print(analogRead(A0));
      //       Serial.print(",");
      //       Serial.println(curr_mic);

      if (average_mic - diviation_mic >= curr_mic or curr_mic >= average_mic + diviation_mic) {
        peaks++;
        Serial.println(curr_mic);

        if (peaks > 50 and secs - first_peak < 300) {
          Serial.println("THUNDER");
          Serial.println(secs - current);
          Serial.print("The lightning is in a radius of ");
          Serial.print(speed_of_sound * (secs - current) / 1000);
          Serial.println("m");
          break;
        }

        else if (peaks == 1) {
          first_peak = secs;
        }
      }
    }
  }
  digitalWrite(r_led, LOW);
}
