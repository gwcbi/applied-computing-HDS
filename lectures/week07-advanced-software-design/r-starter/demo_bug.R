# Run this to see the planted bug in action.
#
# Expected (correct) behavior: mean_by_site() returns a real number for
# every site, even when one of that site's lab values is missing (NA) --
# a missing value should be excluded from the mean, not silently wipe out
# the whole site's summary.
#
# What actually happens: source this file. The DC row's mean_value is NA,
# not the mean of the two valid values (4.2 and 3.8) -- one NA in the input
# silently erases the entire site's summary. No error, no warning.
#
# Debugging exercise (see ../practical.md): devtools::load_all(".") from
# this package's root, then set a breakpoint inside mean_by_site()
# (R/stats.R) -- RStudio's breakpoint gutter or browser() both work -- and
# step through the loop, inspecting site_rows$value for the DC group. Once
# you see what's happening, fix R/stats.R so a single NA doesn't erase the
# whole site's mean. Don't just drop NA rows here in this demo script
# instead.

# devtools::load_all(".")  # run from the r-starter/ package root first

labs <- data.frame(
  site = c("DC", "DC", "DC", "VA", "VA"),
  value = c(4.2, 3.8, NA, 5.0, 5.4)
)

print(mean_by_site(labs))
cat("Bug check: the DC row's mean_value should be a number, not NA.\n")
