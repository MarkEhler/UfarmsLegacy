This is a starter template for [Learn Next.js](https://nextjs.org/learn).


Hi Joseph!

Here's an update about using fetch to dig the Flask framework.  Greek to me xD


// Example using fetch

fetch('/testmap')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
