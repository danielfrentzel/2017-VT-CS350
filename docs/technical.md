<h1>Technical Documentation</h1>

<strong>General Background</strong>: <p>The tour is built with Flask, Python, SQLite, JavaScript, and Jquery. Flask is used for the backend development, including writing and reading the SQL database. When the index is loaded, flask is used to reach into the locations table of the database and place the pin icon at all the locations.</p>


<h2>Index</h2>
<p>A boolean is used to toggle with the button between add and view mode. Each pin was created with an onclick function. </p>

<strong>Viewing Locations</strong>: <p>When the boolean is on view mode, the user must click on a location pin. Upon clicking a pin, a function is called that loads DisplayLocation, remembering the pin id. </p>

<strong>Adding to an existing location</strong>: <p>When the boolean is on add mode, the user can click on and add pictures to an existing pin. This time when the pin is clicked, the user is taken to an upload page using Flask to remember the pin id that was clicked.</p>

<strong>Adding a new location</strong>: <p>When the boolean is on add mode, the user can click on the map where there isn't an exisiting pin to add a new pin. The click triggers a function that open the add location page and memembers the x and y screen coordinates of the click by placing them in the url of the opened page.</p>


<h2>DisplayLocation Page</h2> 
<p>The DisplayLocation page takes the pin id and reaches into the pictures table of the database to see if pictures have been uploaded to the clicked on location. If pictures have been uploaded, an SQL command pulls the images from the given location and displays them in a slide show. If pictures haven't been uploaded, an upload button is displayed so the user can upload images to the clicked on location.</p>


<h2>UploadImg Page</h2> 
<p>The UploadImg page also takes the pin id that was click on. A form is displayed where images can be uploaded or deleted. When a photo is uploaded, the image is placed in the static/imgs folder. Flask takes the image path location and puts it in the picture folder of the database. If a image is being deleted, flask removes the picture from the pictures table of the database.</p>


<h2>AddLocation Page</h2>
<p>The AddLocation page is given the x and y screen coordinates of the pin to be added by Flask. Flask pulls these coordinates from the url and saves them as variables. The user can add a name and a description and submit the form. Flask takes the form and puts it into the locations table of the database. The locations are loaded from the database and displayed. The user can also delete a location, given the location id.</p>
