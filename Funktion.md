# SMS-Heizungs-Fernsteuerung - Funktion

Die Steuerung basiert auf der Software [gammu](https://github.com/gammu/gammu). 
Diese steuert den Empfang und Versand von SMS über den UMTS-Stick. Über 
einen Schrittmotor (28BYJ-48) mit Zahnriemen wird der Drehknopf an der Heizung 
bedient.

Die Konfiguration von gammu ist in **/etc/gammu-smsdrc**. Beim Eintreffen 
einer SMS wird das Skript **/home/matthias/receivedSMS.py** ausgeführt.

Per Cronjob (auf user-Level) wird stündlich die Raumtemperatur gemessen, 
täglich statistische Werte (Durchschnitt, Minimum, Maximum) berechnet und 
montags morgens die Werte des Wochenendes per SMS an mein Handy verschickt:

Aus **crontab -l**:
>   # m h  dom mon dow   command  
> 3 * * * * /home/mabe42/getTemperature.py  
> 5 23 * * * /home/mabe42/calcAvg.py  
> 0 7 * * mon /home/mabe42/sendWeekend.py  
> */2 * * * * /home/mabe42/sendSMS.py  

## getTemperature.py

Die Temperatur wird mit einem DS1820-Temperatursensor, der am 1-wire-Bus des 
Raspi hängt, stündlich gemessen. Die Werte werden in wochentägliche Logfiles 
(~/mon.log usw.) geschrieben, die wöchentlich überschrieben werden.

## calcAvg.py

Einmal täglich abends werden aus dem Logfile des Tags die Durchschnitts-, 
Minimal- und Maximaltemperatur berechnet und in eine entsprechende 
wochentägliche Datei (~/mon.avg usw.) geschrieben. Diese wird ebenfalls 
wöchentlich überschrieben.

## receivedSMS.py

Wenn eine SMS eintrifft, wird dieses Skript gestartet. Je nach Schlüsselwort 
wird eine bestimmte Aktion ausgeführt. Wird keines der bekannten 
Schlüsselwörter erkannt, wird SMS an mein Handy weitergeleitet. Da in diesem 
Skript nicht direkt SMS verschickt werden können, funktioniert der SMS-Versand 
über einen Umweg: Der zu sendende Text wird in **~/content** geschrieben. Alle 
zwei Minuten überprüft **sendSMS.py**, ob diese Datei vorhanden ist und 
verschickt ggf. den Inhalt von **~/content** als SMS an mein Handy.

Je nach Schlüsselwort eine entsprechende Aktion ausgeführt:

* Reboot: Reboot des Raspi.
* Status: Eine Status-Meldung wird per SMS versendet (**~/sendStatus.py**)
* Restsms: Nach der Aufladung des Guthabens kann die neu berechnete zur 
  Anszahl der SMS, die zur Verfügung steht, auf den Raspi übertragen werden. 
  Diese Zahl wird in **~/restsms** gespeichert.
* Stufe: Hier wird die Heizung auf eine Stufe von 0-10 gestellt 
  (**~/turnSteps.py**). Der Wert wird in **~/heizungsStufe** gespeichert.

## sendSMS.py

Wenn **~/content** vorhanden ist, wird der Inhalt von **~/content** an mein 
Handy geschickt. Danach wird **~/content** gelöscht.

## sendStatus.py

Aktuelle Temperatur, aktuelle Stufe der Heizung, Anzahl der RestSMS, uptime, 
Datum und Uhrzeit werden in **~/content** geschrieben, so dass diese beim 
nächsten Aufruf von **sendSMS.py** an mein Handy geschickt werden. 

## turnSteps.py

Dreht den Schrittmotor entsprechend. Das Programm habe ich von 
<http://www.elektronx.de/tutorials/schrittmotorsteuerung-mit-dem-raspberry-pi/> 
übernommen.

## sendWeekend.py

Montag morgens werden die Temperaturdaten der vergangenen drei Tage, die 
aktuelle Stufe der Heizung und die Anzahl der RestSMS in  **~/content** 
geschrieben, so dass diese beim nächsten Aufruf von **sendSMS.py** an mein 
Handy geschickt werden. 
