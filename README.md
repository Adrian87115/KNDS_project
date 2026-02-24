# Klasyfikacja Rezerwacji Hotelowych

**Projekt KNDS**
**Autorzy:** Adrian Lyubezny, Adrian Lusztyk, Szymon Domański

---

## Cel i kontekst biznesowy
Anulowane rezerwacje stanowią istotną stratę finansową i logistyczną dla działalności hotelu. Głównym celem projektu było opracowanie modelu uczenia maszynowego, który z wysoką precyzją pozwoli identyfikować rezerwacje obarczone ryzykiem rezygnacji. Analiza została przeprowadzona na zbiorze danych Hotel Reservations Dataset.

## Eksploracyjna Analiza Danych (EDA)
W ramach analizy danych sformułowano następujące kluczowe wnioski:

* **Skala problemu:** Około 33% wszystkich rezerwacji w badanym zbiorze kończy się anulowaniem, co znacząco wpływa na płynność finansową obiektu.
* **Złożoność cech:** Macierz kowariancji wykazała brak pojedynczej zmiennej dominującej; decyzja o anulowaniu zależy od splotu wielu czynników i braku silnych korelacji liniowych z cechą docelową.
* **Lead Time:** Czas wyprzedzenia rezerwacji jest najsilniejszym predyktorem - im wcześniej dokonano rezerwacji, tym większe prawdopodobieństwo rezygnacji.
* **Punkt krytyczny:** W przypadku rezerwacji dokonywanych z wyprzedzeniem powyżej 90 dni, współczynnik anulowań wzrasta do poziomu 57%.
* **Lojalność gości:** Powracający klienci (Repeat Guests) stanowią najbardziej stabilną grupę i niemal nigdy nie odwołują rezerwacji.
* **Zaangażowanie:** Goście zgłaszający dodatkowe prośby specjalne (Special Requests) anulują rezerwacje dwukrotnie rzadziej (20%) niż osoby bez żadnych wymagań (ponad 40%).
* **Segmentacja rynku:** Najwięcej odwołań generuje segment "Online", podczas gdy rezerwacje korporacyjne i uzupełniające (Complementary) charakteryzują się bardzo niskim ryzykiem rezygnacji.
* **Wpływ ceny:** Wyższa średnia cena za pokój (avg_price_per_room) koreluje z wyższą skłonnością gości do szukania alternatyw i anulowania rezerwacji w ostatniej chwili.

## Porównanie modeli i wyniki
W procesie modelowania przetestowano kilka algorytmów klasyfikacyjnych. Poniższa tabela przedstawia wyniki na zbiorze testowym:

| Model | Accuracy | F1-Score (klasa 1) | Precision (klasa 1) | Recall (klasa 1) |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | **0.91** | **0.93** | **0.92** | **0.95** |
| CatBoost | 0.89 | 0.92 | 0.90 | 0.94 |
| MLP Classifier | 0.87 | 0.93 | 0.88 | 0.90 |
| Logistic Regression | 0.81 | 0.87 | 0.83 | 0.90 |

## Najlepszy model
Najwyższą skuteczność osiągnął model **Random Forest**.

* **Metryki:** Model uzyskał wynik ROC AUC na poziomie 0.9584.
* **Optymalne parametry:** n_estimators: 200, max_depth: 20, min_samples_split: 2, min_samples_leaf: 1.
* **Wydajność:** Model poprawnie zidentyfikował 4636 rezerwacji zrealizowanych (True Positives), wykazując dużą odporność na błędy klasyfikacji mimo braku silnych zależności liniowych w danych wejściowych.

## Rekomendacje biznesowe
* **Polityka zaliczek:** Rekomenduje się wprowadzenie obowiązkowych bezzwrotnych zaliczek dla rezerwacji dokonywanych z wyprzedzeniem przekraczającym 90 dni.
* **Monitoring segmentów:** Należy objąć szczególnym nadzorem rezerwacje pochodzące z kanału "Online" oraz te o cenie powyżej średniej rynkowej.
* **Programy lojalnościowe:** Warto intensyfikować działania zmierzające do przekształcania gości jednorazowych w gości powracających, ze względu na ich marginalny wskaźnik anulowań.
