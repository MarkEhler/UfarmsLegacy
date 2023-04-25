var map = L.map('map').setView([latitude, longitude], zoom);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(map);

var marker = L.marker([latitude, longitude]).addTo(map);
marker.bindPopup("<b>Your Location</b>").openPopup();
