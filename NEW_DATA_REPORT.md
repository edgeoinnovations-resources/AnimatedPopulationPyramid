# UN World Population Prospects 2024 - Data Report

**File:** `1 unpopulation_dataportal_20251228214054.csv`
**Generated:** December 28, 2025

---

## File Summary

| Attribute | Value |
|-----------|-------|
| **Total Rows** | 813,645 |
| **Total Columns** | 27 |
| **Memory Size** | ~842 MB |
| **Source** | United Nations Population Division |
| **Dataset** | World Population Prospects 2024 |

---

## Data Coverage

| Dimension | Coverage |
|-----------|----------|
| **Locations** | 314 (countries + regions) |
| **Years** | 1990-2030 (41 years) |
| **Sex Categories** | Male, Female, Both sexes |
| **Age Groups** | 21 five-year groups (0-4 through 100+) |
| **Variant** | Median projection |
| **Estimate Type** | Model-based Estimates |

---

## Column Definitions

| Column | Type | Description |
|--------|------|-------------|
| `IndicatorId` | int | Numeric indicator ID (46) |
| `IndicatorName` | str | "Population by 5-year age groups and sex" |
| `IndicatorShortName` | str | Short description |
| `Source` | str | "World Population Prospects" |
| `SourceYear` | int | 2024 |
| `Author` | str | "United Nations Population Division" |
| `LocationId` | int | UN location code |
| `Location` | str | Country/region name |
| `Iso2` | str | ISO 2-letter code |
| `Iso3` | str | ISO 3-letter code |
| `TimeId` | int | Time period ID |
| `Time` | int | Year (1990-2030) |
| `VariantId` | int | Projection variant ID |
| `Variant` | str | "Median" |
| `SexId` | int | 1=Male, 2=Female, 3=Both |
| `Sex` | str | "Male", "Female", "Both sexes" |
| `AgeId` | int | Age group ID |
| `AgeStart` | int | Start of age range (0, 5, 10...) |
| `AgeEnd` | float | End of age range (4, 9, 14...) |
| `Age` | str | Age label ("0-4", "5-9"...) |
| `CategoryId` | int | Category ID |
| `Category` | str | "Not applicable" |
| `EstimateTypeId` | int | Estimate type ID |
| `EstimateType` | str | "Model-based Estimates" |
| `EstimateMethodId` | int | Method ID |
| `EstimateMethod` | str | "Projection" |
| `Value` | float | **Population count** |

---

## Age Groups (21 total)

| Group | Age Range |
|-------|-----------|
| 0-4 | Infants & toddlers |
| 5-9 | Early childhood |
| 10-14 | Pre-teens |
| 15-19 | Teenagers |
| 20-24 | Young adults |
| 25-29 | |
| 30-34 | |
| 35-39 | |
| 40-44 | |
| 45-49 | |
| 50-54 | |
| 55-59 | |
| 60-64 | Near retirement |
| 65-69 | Early elderly |
| 70-74 | |
| 75-79 | |
| 80-84 | |
| 85-89 | |
| 90-94 | |
| 95-99 | |
| 100+ | Centenarians |

---

## Data Quality

| Issue | Count | Percentage |
|-------|-------|------------|
| Missing `Iso2` | 2,583 | 0.32% |
| Missing `AgeEnd` | 38,745 | 4.76% |

**Note:** Missing `AgeEnd` values are for the "100+" age group (no upper bound).
Missing `Iso2` values are for aggregate regions (e.g., "World", "Africa").

---

## Key Statistics

### Population Value Range
- **Minimum:** 0
- **Maximum:** 697,928,079 (China, 0-4 age group in early 1990s)
- **Mean:** 8,765,239
- **Median:** 130,718

### Value Distribution
The data is highly right-skewed due to:
- Small countries (Vatican, Nauru) with values near 0
- Large countries (China, India) with values in hundreds of millions
- Aggregate regions (World, Asia) with billions

---

## Top 10 Most Populous Entities (2024)

| Rank | Location | Population |
|------|----------|------------|
| 1 | World | 8.16 billion |
| 2 | Developing regions | 6.88 billion |
| 3 | Low-and-middle-income countries | 6.87 billion |
| 4 | Middle-income countries | 6.11 billion |
| 5 | Less developed regions (excl. LDCs) | 5.69 billion |
| 6 | Developing regions (excl. China) | 5.43 billion |
| 7 | Asia | 4.81 billion |
| 8 | High-and-upper-middle-income countries | 4.08 billion |
| 9 | Low-and-lower-middle-income countries | 4.05 billion |
| 10 | Lower-middle-income countries | 3.29 billion |

---

## Youngest Populations (2024)
**Percentage of population under age 15**

| Rank | Country | Youth % |
|------|---------|---------|
| 1 | Central African Republic | 49.0% |
| 2 | Niger | 46.6% |
| 3 | Somalia | 46.6% |
| 4 | Mali | 46.1% |
| 5 | Chad | 46.1% |
| 6 | DR Congo | 46.0% |
| 7 | Middle Africa (region) | 44.8% |
| 8 | Burundi | 44.7% |
| 9 | Mozambique | 44.5% |
| 10 | Angola | 44.4% |

---

## Oldest Populations (2024)
**Percentage of population age 65+**

| Rank | Country | Elderly % |
|------|---------|-----------|
| 1 | Monaco | 36.2% |
| 2 | Japan | 29.8% |
| 3 | Saint Helena | 26.9% |
| 4 | Martinique | 25.3% |
| 5 | Puerto Rico | 24.7% |
| 6 | Italy | 24.6% |
| 7 | Portugal | 24.5% |
| 8 | Greece | 23.9% |
| 9 | Guadeloupe | 23.9% |
| 10 | Finland | 23.9% |

---

## Geographic Notes

The dataset includes:
- **237 countries/territories** (sovereign nations, dependencies, territories)
- **77 aggregate regions** (continents, income groups, development classifications)

Examples of aggregate regions:
- World
- Africa, Asia, Europe, Oceania, Americas
- High-income countries, Low-income countries
- Least developed countries (LDCs)
- Small Island Developing States (SIDS)
- Landlocked Developing Countries (LLDCs)

---

## Recommended Use Cases

1. **Population Pyramids** - Age/sex distribution visualization
2. **Demographic Transition Analysis** - Track aging populations over time
3. **Dependency Ratio Calculations** - Youth + elderly vs working age
4. **Population Projections** - 2024-2030 projections included
5. **Regional Comparisons** - Built-in aggregate regions

---

## Citation

```
United Nations, Department of Economic and Social Affairs,
Population Division (2024). World Population Prospects 2024,
Online Edition.
```
