# Aleksejs-Kondratjevs-projekts-Bitcoin
## Projekts Bitcoin
Šis projekts ir izstrādāts kā automatizēts risinājums, lai uzraudzītu Bitcoin (BTC) kursa izmaiņas attiecībā pret ASV dolāru (USD). Galvenais mērķis ir nodrošināt, ka lietotājs tiek informēts par būtiskām kursa izmaiņām, kas var ietekmēt viņa investīciju lēmumus.

**Izmantotās Python bibliotēkas:**
* requests: Izmanto, lai veiktu HTTP pieprasījumus uz Livecoinwatch API, lai iegūtu Bitcoin kursa datus.

* schedule: Ļauj ieplānot regulāru kursa pārbaudi, šajā gadījumā ik pēc 10 sekundēm.

* time: Izmanto, lai kontrolētu laika intervālus skripta izpildes laikā.

* smtplib, email.mime.text un email.mime.multipart: Izmanto, lai veidotu un nosūtītu e-pastu par kursa izmaiņām.

**Metodes:**

  1. Metode **get_btc_data** izsauc HTTP POST pieprasījumu, lai iegūtu un atgrieztu Bitcoin (BTC) kursu ASV dolāros no Livecoinwatch API. Tā sūta nepieciešamo API atslēgu un pieprasījuma datus JSON formātā, un pēc tam atgriež API atbildi kā JSON objektu. previous_data ir globālais mainīgais, kas izmantots, lai saglabātu iepriekšējo BTC kursu starp pieprasījumiem.
  
 2.  Metode **check_data_and_notify** veic divas galvenās funkcijas: 
 - Kursa Izmaiņu Pārbaude: Tā pārbauda pašreizējās Bitcoin (BTC) kursa izmaiņas. Ja tas ir pirmās izsaukšanas reizes, metode saglabā kursu globālajā mainīgajā **previous_data.** Ja kursa izmaiņa ir 0.50 ASV dolāri vai vairāk salīdzinājumā ar iepriekšējo reizi, tā turpina uz nākamo soli. 
 - Paziņojuma Nosūtīšana: Ja ir konstatēta nozīmīga kursa izmaiņa, metode izsauc funkciju **send_email**, lai nosūtītu e-pastu ar informāciju par pašreizējo BTC kursu un tā nosaukumu. Pēc tam atjaunina **previous_data** ar jaunāko kursu.
3. Metode send_email ir paredzēta e-pasta nosūtīšanai ar informāciju par Bitcoin (BTC) kursu. Tā izveido e-pasta ziņojumu, norādot sūtītāja un saņēmēja adreses un ziņojuma tēmu. Ziņojuma ķermenī tiek iekļauta informācija par Bitcoin nosaukumu un kursu. Pēc tam, izmantojot smtplib bibliotēku, tiek izveidots savienojums ar SMTP serveri ('smtp.office365.com'), tiek izsaukta **starttls()** funkcija drošībai, un tiek veikts pieslēgšanās solis, izmantojot norādīto e-pasta adresi un paroli. Ja viss notiek veiksmīgi, ziņojums tiek nosūtīts; ja rodas kādas kļūdas, tās tiek izdrukātas. Beigās servera savienojums tiek pārtraukts.

5. Metode izmanto schedule bibliotēku, lai ieplānotu metodes **check_data_and_notify** izpildi ik pēc 10 sekundēm. Metode **check_data_and_notify** tiks automātiski izsaukta katras 10 sekundes, lai pārbaudītu Bitcoin kursa izmaiņas un nepieciešamības gadījumā nosūtītu e-pastu par šīm izmaiņām.

## Projekta gaitā

Pirms Bitcoin projekta es mēģināju izveidot laika apstākļu parādīšanas projektu - es arī mēģināju izstrādāt programmu, kas varētu parādīt laika apstākļus. Šīs programmas mērķis bija sniegt lietotājiem aktuālu informāciju par laika apstākļiem viņu norādītajās vietās. Problēma projekta pildīšanas laikā - lai iegūtu nepieciešamo informāciju, bija jāizmanto laika apstākļu API, taču lai iegūtu piekļuvi šim API, bija nepieciešams veikt samaksu. Tā kā šis projekts bija paredzēts kā bezmaksas risinājums, es nolēmu izstrādāt bezmaksas projektu.

***Nākotnes iespējas:***
*Ir iespējams meklēt alternatīvus bezmaksas API vai izstrādāt risinājumu ar ierobežotām funkcijām, izmantojot pieejamos bezmaksas API. Projekts demonstrē Python valodas spēju tikt galā ar dažādiem uzdevumiem, izmantojot tās plašo bibliotēku klāstu. Tomēr tie arī atklāj izstrādes procesā sastopamos izaicinājumus, piemēram, nepieciešamību pēc maksas API piekļuves, lai nodrošinātu pilnu funkcionalitāti.*
