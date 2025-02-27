<h1 align = center >HABIT TRACKER</h1>

<p>This project aims to develop a habit tracking application leveraging the Pixela API to automate the creation, management, and visualization of user habits. The application allows users to create a new account, set up custom habit-tracking graphs, and log daily activities through a Python script. By utilizing the Pixela API, users can easily monitor their progress over time, aiding in the development of consistent habits and achieving personal goals.

The script begins by creating a user account on Pixela, requiring the user to agree to the terms of service and confirm they are not a minor. Once the account is set up, the application proceeds to create a customizable graph that tracks a specific habit, such as coding hours. This graph configuration includes attributes like the graph's ID, name, unit of measurement, data type, and color.

After setting up the graph, the application allows users to log their daily habit activities by sending POST requests to the Pixela API. The logs include the date and the quantity of the habit tracked, which are then visualized on the graph. The application also includes functionalities to retrieve and analyze the logged data, providing users with insightful visual feedback on their habit development.

This project showcases the integration of RESTful APIs in Python to automate user interactions with external services, demonstrating the practical use of programming in enhancing personal productivity and habit formation..</p>
