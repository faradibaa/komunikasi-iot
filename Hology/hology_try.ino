// https://randomnerdtutorials.com/telegram-esp8266-nodemcu-motion-detection-arduino/

#include <HCSR04.h> // HCSR04 ultrasonic sensor (by gamegine)
#include <Servo.h>
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// sensor: HC-SR04
// aktuator: servo, LCD, chatbot

// variabel yang dibutuhkan
float distance = 0, threshold = 0; // jarak, batas
int degree = 0; // sudut gerak servo

// menyambungkan ke WiFi
const *char ssid = "Nyanko";
const *char pass = "meongnyan";

// inisialisasi telegram bot
#define TOKEN "5711045728:AAEnTxM37bzVPXFr-nCxALZuXShOHTWAH9c"

// Use @myidbot to find out the chat ID of an individual or a group
// Also note that you need to click "start" on a bot before it can
// message you
#define BOT_ID "1025656101"

HCSR04 hc(5, 6); // trig pin, echo pin
Servo servo;
X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(TOKEN, client);

void setup() {
  Serial.begin(9600);
  client.setTrustAnchors(&cert); // menambahkan root certificate untuk api.telegram.org
}

void loop() {
  // mengkoneksikan ke WiFi
  Serial.print("Connecting Wifi: ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA); // ini buat apa ya?
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  // Sensor ultrasonik
  distance = hc.dist();
  Serial.print("Jarak yang terbaca: "); // mengecek jarak yang terbaca sensor
  Serial.println(distance);
  if(distance < threshold) {
    // Chatbot telegram
    bot.sendMessage(BOT_ID, "Bot started up", "");
    Serial.println("Notifikasi telah dikirim ke telegram!");
  }

  // Servo
  servo.write(degree); // buka
  delay(2000); // sesuaikan sama berapa lama tutup dibuka
  servo.write(0); // tutup
  delay(20);
}
