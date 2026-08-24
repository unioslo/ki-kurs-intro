
Sett 1
==================

.. uio-task::    Oppgave 1: Instruksjoner

   Utforsk 2 ulike KI-tjenestene og øv på ulike teknikker for å gi instruksjoner.
   Diskuter gjerne med en kollega hvordan og hva de ulike tjeneste fungerer til.

.. uio-task:: Oppgave 2 - Idegenerering

   Spør et KI-verktøy om å generere 10 ideer til hvordan KI kan brukes i din arbeidshverdag.
   Spesifiser tydelig hva slags oppgaver du gjør og hvilke verktøy du har tilgjengelig.

.. uio-task:: Oppgave 3 - Gemini Notebook

   Last opp et dokument i Gemini Notebook. Velg et dokument som er relevant for jobben din, eller et dokument du er interessert i.
   Lag et tankekart og en studieveiledning, og still spørsmål om dokumentets innhold.

.. uio-task:: Oppgave 4 - Opprettelse av maler

   Tenk på et arbeidsområde hvor du lager lignende dokumenter eller tekster ofte.
   Bruk et av de tilgjengelige KI-verktøyene til å lage et forslag til en mal du kan bruke i arbeidet ditt.

.. uio-task:: Oppgave 5 - KI-assistent

   Sett opp din helt egne KI-assistent i GPT UiO.

   1. Velg én oppgave du gjør ofte (f.eks. svare på henvendelser, lage agenda, oppsummere møter).
   2. Lag en "standard-instruksjon" som du kan bruke igjen, som beskriver:
      - Din rolle og arbeidsfelt
      - Typisk målgruppe
      - Ønsket stil og format
   3. Test instruksjonen på et eksempel fra jobben.
   4. Juster instruksjonen til du har en versjon du kan bruke som mal fremover.

.. uio-task:: Oppgave 6 - Bildegenering

   Du skal kalle inn til et møte med valgfritt tema.
   Be Copilot om å generere et relevant bilde du kan bruke i møteinnkallelsen.

.. uio-task:: Oppgave 7 - Powerpoint

   Be Copilot lage en utkast til en powerpoint-presentasjon om et valgfritt tema.


.. uio-task:: Oppgave 8 - Enkel programmering

   Vi ønsker at excel skal summere tallene i to kolonner automatisk.

   .. figure:: ../images/excel-snutt.png
      :align: center
      :width: 50%
      :alt: Skjermdump utsnitt av et excel ark med 3 kolonner.

   For å få til dette har vi skrevet en kort makro:

   ::

      Sub LeggTilTall()
         Dim sisteRad As Long
         Dim i As Long

         sisteRad = Cells(Rows.Count, 1).End(xlUp).Row

         For i = 2 To sisteRad ' Antar at første rad er header

         Cells(i, 3).Value = Cells(i, 1).Value + Cells(i, 1).Value
      Next i
      End Sub

   Dessverre inneholder denne kodesnutten en feil, og summene vi får stemmer ikke med forventningene.

   - Oppgave 1: Få GPT til å forklare hva som er feil med kodesnutten, og hvorfor den ikke gir summen av kolonne A og B.
   - Oppgave 2: Få GPT til å skrive en riktig versjon av koden som faktisk gir summen av kolonne A og B.

   Oppgaven kan løses utelukkende med kodesnutten over og GPT UiO,
   men for de som eventuelt er ekstra nysgjerrige ligger det en excel-fil med den beskrevne funksjonaliteten om man vil teste det selv her: `Enkel-koding-med-KI.xlsx <https://uio.instructure.com/courses/63248/files/3954949/download>`_

.. uio-source::

   Takk til `ØVA <https://www.uio.no/om/organisasjon/fellesadm/ova/>`_ som har delt sine KI_oppgaver med oss!
