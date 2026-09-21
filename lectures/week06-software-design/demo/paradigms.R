# Same task as paradigms.py, in R: given each patient's BMI, classify into
# a weight-status category.
#
# R leans functional/vectorized by default -- most R code you'll encounter
# (base R and tidyverse alike) IS the "functional" style below, not the
# procedural loop. This script shows why: the vectorized version is both
# shorter and faster (no explicit loop), because R's operators already work
# element-wise over a whole vector.
#
# Live-demo script for Week 6 -- lecture segment 2, "Software design
# paradigms." R side of the Python/R comparison in paradigms.py.
# Run it:
#   Rscript paradigms.R

patients <- data.frame(
  patient_id = c("P001", "P002", "P003", "P004"),
  bmi        = c(17.8, 22.4, 27.1, 33.6),
  stringsAsFactors = FALSE
)

# --------------------------------------------------------------------
# 1. Procedural -- an explicit loop, mutating a result vector as it goes.
#    This is idiomatic in many languages but is NOT idiomatic R -- most
#    experienced R users would flag this as "written like Python/C."
# --------------------------------------------------------------------
bmi_category_procedural <- function(bmi_values) {
  categories <- character(length(bmi_values))
  for (i in seq_along(bmi_values)) {
    bmi <- bmi_values[i]
    if (bmi < 18.5) {
      categories[i] <- "underweight"
    } else if (bmi < 25) {
      categories[i] <- "normal"
    } else if (bmi < 30) {
      categories[i] <- "overweight"
    } else {
      categories[i] <- "obese"
    }
  }
  categories
}

# --------------------------------------------------------------------
# 2. Functional / vectorized -- no explicit loop. `cut()` classifies the
#    entire vector at once; this is the idiomatic R way to do this task.
# --------------------------------------------------------------------
bmi_category_functional <- function(bmi_values) {
  as.character(cut(
    bmi_values,
    breaks = c(-Inf, 18.5, 25, 30, Inf),
    labels = c("underweight", "normal", "overweight", "obese"),
    right = FALSE
  ))
}

# --------------------------------------------------------------------
# 3. A light OOP note (S3) -- R supports OOP too (S3, S4, R6), but it's
#    used far less often for this kind of task than the vectorized
#    approach above. Shown here for completeness, not as the recommended
#    way to solve this particular problem.
# --------------------------------------------------------------------
new_patient <- function(patient_id, bmi) {
  structure(list(patient_id = patient_id, bmi = bmi), class = "patient")
}

bmi_category.patient <- function(p) {
  bmi_category_functional(p$bmi)
}

cat("Procedural:\n")
print(bmi_category_procedural(patients$bmi))

cat("\nFunctional/vectorized:\n")
print(bmi_category_functional(patients$bmi))

cat("\nS3 OOP (one patient, for illustration only):\n")
one <- new_patient("P004", 33.6)
print(bmi_category.patient(one))
