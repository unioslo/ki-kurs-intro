
Et praktisk eksempel
====================

La oss se på et konkret eksempel:

.. code-block:: text

   DU: "Hva er åpningstidene til biblioteket på Blindern?"

**Hva skjer i modellen:**

1. Modellen ser at dette er et spørsmål om åpningstider
2. Den har sett mange lignende spørsmål under trening
3. Den har lært mønsteret: spørsmål om åpningstider → svar med tider
4. Den genererer et svar som *ser ut* som åpningstider

**Problemet:**

Modellen kan konstruere et helt plausibelt svar som "Biblioteket på Blindern er åpent 08:00-20:00 mandag-fredag og 10:00-16:00 i helgene" - selv om dette er fullstendig feil!

.. uio-dont::

   **Modellen "vet" ikke hva åpningstidene faktisk er. Den genererer bare tekst som ligner på svar om åpningstider.**
