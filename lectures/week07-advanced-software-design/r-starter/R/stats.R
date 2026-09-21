#' Compute mean lab value by site
#'
#' Groups a data frame of patient lab values by `site` and returns the mean
#' `value` for each site. This function exists for Week 7's packaging +
#' debugging exercise -- intentionally tiny, one function, one planted bug.
#'
#' @param df A data frame with columns `site` (character) and `value`
#'   (numeric) -- e.g. one row per lab result.
#'
#' @return A data frame with one row per site and its mean `value`.
#'
#' @export
mean_by_site <- function(df) {
  sites <- unique(df$site)
  result <- data.frame(site = sites, mean_value = numeric(length(sites)))
  for (i in seq_along(sites)) {
    site_rows <- df[df$site == sites[i], ]
    result$mean_value[i] <- mean(site_rows$value)
  }
  result
}
