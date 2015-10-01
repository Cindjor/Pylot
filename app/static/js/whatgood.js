

<script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
<script src="https://maps.googleapis.com/maps/api/js"></script>

function initialize() {
		alert(1);
        var mapCanvas = document.getElementById('map');
        var mapOptions = {
          center: new google.maps.LatLng(37.279518, -121.8679),
          zoom: 8,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions)
      }

      $(document).ready(function(){
      google.maps.event.addDomListener(window, 'load', initialize);
  	}
