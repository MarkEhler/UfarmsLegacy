<h1> Ufarms </h1>
<h2> ToC </h2>
<ul>
    <li> app/ -- flask package files</li>
    <li> run.py -- init file for flask</li>
    <li> Local Reproduction Steps </li>
    <li> Additional info below </li>
    <li> <a href="#"> Demo Video - coming soon </a> </li>

<h2> Setting up a Local Flask Environment  </h2>

<ul> 
<li>run `python venv venv` in root directory </li>
<li>`source venv/bin/activate` </li>
<li>Git clone this repo </li>
<li>Change directory to the repo </li>
<li>`pip install -r requirements.txt` </li>
<li>Copy paste `.flaskenv` file from the note (You do have the note don't you?) </li>
<li>See that the .crt file exists in your local the path defined in __init__.py(maybe differ for windows and apple users) </li>
<li> `flask run` in Ufarms directory </li>
<li>Observe requests to the server on localhost:5000 in this terminal </li>
</ul>

<h2> Set up the Front End </h2>
<li> requires npm & Node.js and if want, Yarn to be installed </li>
<li> open a second terminal </li>
<li> `cd client` then `npm install` or update all dependencies with yarn</li>
<li> `npm run dev` or `yarn start` </li>
<li> Observe changes to your code in real time on http://localhost:3000 </li>

<h2> The Verdant Vision </h2>
<br>
<br>
    <p>
    The goal of this project is to create a community for people to connect around local agriculture projects.  Supermarkets, kitchens, grain mills, barns, what do all these places have in common?  We gather(ed) in them and we go to them to get the food.  Over time, these meeting places have been cut off or replaced by unsustainable food supply networks.  While our curreny grocery supply chain is an impressive feat of modern logistics, it places avaibility above any other expense and wastes a large amount of the food we grow.
    <figure>
    <a href="https://imgur.com/pDNLKEg"><img src="https://i.imgur.com/pDNLKEg.png" title="food waste" /></a>
    <figcaption style="font-size: smallest;">
        <a href="https://19january2021snapshot.epa.gov/facts-and-figures-about-materials-waste-and-recycling/food-material-specific-data_.html" target="_blank">
        US EPA 2021
        </a>
    </figcaption>
    <br>
    </figure>
    In the process seem to have lost our ability to care for the land and eachother.  Ufarms is about seeing a world where everyone living in cities has access to grow their own food and connect with their neighbors again.
    </p>
<br>
<br>

<h2> How it's Intended to Grow </h2>
    <br>
    <body> At it's core, this project is meant to do two things, collect a list of farmers and land owners and show them the map so they can connect.  First a map, then we can find the way back.  This mockup is intended to convey a fully functioning map module.
    <a href="https://imgur.com/aNEB4nB"><img src="https://i.imgur.com/aNEB4nB.jpg" title="mockup" style="border: 2px solid #000;">
    </a>

<h3> Call to action </h3>
    <br>
    <p>At this phase we only need your intrest.  Contributing to a healthier food system doesn't need to be hard, it can acutally be kinda fun.  If you're intrested in being included in the beta, drop us a line!</p>
    <br>
<h2> Get in Touch </h2>
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSdMcVM9-m9wIySnytV_PTfDHVxrya5ecNSrDL7TunFNzehZYw/viewform?embedded=true"> Mailing List </a> 
    <div class="btn-group open">
        <a class="btn btn-default" href="https://www.linkedin.com/in/mark-ehler-85052548/"> Linkedin</a>
        <a class="btn btn-default" href="https://github.com/MarkEhler"> Github</a>
        <a> <span class="hidden"> m.ehler@comcast.net </span></a>
    </div>
