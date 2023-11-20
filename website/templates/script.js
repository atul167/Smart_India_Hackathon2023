let map;

function initMap() {
  const initialLocation = { lat: 37.7749, lng: -122.4194 }; // San Francisco, CA as the initial location
  map = new google.maps.Map(document.getElementById('map'), {
    center: initialLocation,
    zoom: 8
  });

  // Add a click event listener to the map
  map.addListener('click', (event) => {
    displayLatLng(event.latLng);
  });
}

function displayLatLng(latLng) {
  const infoWindow = new google.maps.InfoWindow();
  infoWindow.setContent(`Latitude: ${latLng.lat()}, Longitude: ${latLng.lng()}`);
  infoWindow.setPosition(latLng);
  infoWindow.open(map);
}
