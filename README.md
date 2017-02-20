# FIX
Testing API on Python with using Allure+pytest
<table style="width:100%">
  <tr>
    <th>Automated</th>
    <th>Severity</th>
    <th>Name</th>
    <th>Request type</th>
    <th>Type of test</th>
    <th>URL</th>
    <th>Parameters</th>
    <th>Expected code</th>
    <th>Expected response</th>
  </tr>
  <tr>
    <th>x</th>
    <th>Critical</th>
    <th>Login – successful</th>
    <th>POST</th>
    <th>Positive</th>
    <th>/api/login</th>
    <th>{"email": "peter@klaven", "password": "cityslicka"}</th>
    <th>200</th>
    <th>{"token": "QpwL5tke4Pnpja7X" }</th>
  </tr>
  <tr>
    <th>x</th>
    <th>Critical</th>
    <th>Login – w/o email</th>
    <th>POST</th>
    <th>Negative</th>
    <th>/api/login</th>
    <th>{"password": "cityslicka"}</th>
    <th>400</th>
    <th>{"error": "Missing email" }</th>
  </tr>
 </table>
