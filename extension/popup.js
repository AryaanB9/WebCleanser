function transfer() {
  chrome.tabs.getSelected(null, function (tab) {
    const original_url = tab.url
    
    // URL that will be displayed in the extension
    let tablink = tab.url;
    if (tablink.length > 35) {
      tablink = tablink.slice(0, 35) + ' ...';
    }
    $('#site').text(tablink);
    
    // Sending the URL to index.php in order to run the python code for testing the safety of website
    var xhr = new XMLHttpRequest();
    params = 'url=' + original_url;
    var markup = 'url=' + original_url + '&html=' + document.documentElement.innerHTML;
    xhr.open('POST', 'http://localhost/DJ22Trial3/test/index.php', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = () => {
      if (xhr.responseText === 'SAFE') {
        $('#div1').text(xhr.responseText);
      }
      else if (xhr.responseText === 'SUSPICIOUS') {
        $('#div2').text(xhr.responseText);
      }  
      else if (xhr.responseText === 'MALICIOUS'){
        $('#div3').text(xhr.responseText);
      }
      else {
        // Incase an error occurs then it will displayed as an alert
        alert(xhr.responseText);
      }
      return xhr.responseText;
    };
    xhr.send(markup);
  });
}

// For the loading animation
$(document).ready(function () {
  $('button').click(function() {
    $("#loader-gif").show();
    $("#div-gif").show();
    setTimeout(function() {
      $("#loader-gif").hide();
    }, 9000);
    var val = transfer();
  });
});