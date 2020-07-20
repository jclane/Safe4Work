function copyURL(urlToLoad) {
  document.getElementById("address").value = urlToLoad;
  document.forms["url-form"].submit();
}
