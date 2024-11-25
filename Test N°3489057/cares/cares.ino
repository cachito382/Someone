#include <SPI.h>
#include <Ethernet.h>

// Configuración de la dirección MAC y IP estática (o puedes usar DHCP)
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xFE, 0xFE, 0xED };
IPAddress ip(192, 168, 100, 20); // La IP del Arduino
EthernetServer server(80); // Puerto TCP para el servidor

void setup() {

  pinMode(LED_BUILTIN , OUTPUT);

  // Inicia la comunicación serial
  Serial.begin(9600);
  
  // Inicia la comunicación Ethernet
  Ethernet.begin(mac, ip);
  server.begin();
  
  Serial.println("\nServidor Ethernet iniciado");
}

void loop() {
  // Espera a que haya un cliente conectado
  EthernetClient client = server.available();
  
  if (client) {
    Serial.println("\n Cliente conectado");
    
    // Lee los datos que vienen del cliente
    if (client.available()) {
      
      char c = client.read();

        if(c=='1'){ digitalWrite(LED_BUILTIN , HIGH);}

        if(c=='A'){ digitalWrite(LED_BUILTIN , LOW);}

    }
 
    // Cierra la conexión
    client.stop();
    Serial.println("\n Cliente desconectado");
  }
}
