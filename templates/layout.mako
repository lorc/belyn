# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Belyn - Home media server</title>
    <meta name="author" content="Volodymyr Babchuk">
    <link rel="shortcut icon" href="/static/favicon.ico">
    <link rel="stylesheet" href="/static/bootstrap.css">
    <style type="text/css">
      /* Override some defaults */
      html, body {
        background-color: #eee;
      }
      body {
        padding-top: 40px; /* 40px to make the container go all the way to the bottom of the topbar */
      }
      .container > footer p {
        text-align: center; /* center align it with the container */
      }
      .container {
        width: 960px; /* downsize our container to make the content feel a bit tighter and more cohesive. NOTE: this removes two full columns from the grid, meaning you only go to 14 columns and not 16. */
      }

      /* The white background content wrapper */
      .container > .content {
        background-color: #fff;
        padding: 20px;
        margin: 0 -20px; /* negative indent the amount of the padding to maintain the grid system */
        -webkit-border-radius: 0 0 6px 6px;
           -moz-border-radius: 0 0 6px 6px;
                border-radius: 0 0 6px 6px;
        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.15);
           -moz-box-shadow: 0 1px 2px rgba(0,0,0,.15);
                box-shadow: 0 1px 2px rgba(0,0,0,.15);
      }

      /* Page header tweaks */
      .page-header {
        background-color: #f5f5f5;
        padding: 20px 20px 10px;
        margin: -20px -20px 20px;
      }

      /* Styles you shouldn't keep as they are for displaying this base example only */
/*      .content .span10,
      .content .span4 {
        min-height: 500px;
      } */
      /* Give a quick and non-cross-browser friendly divider */
/*      .content .span4 {
        margin-left: 0;
        padding-left: 19px;
        border-left: 1px solid #eee;
      } */

      .topbar .btn {
        border: 0;
      }

    </style>

  </head>
  <body>
    <div class="topbar">
      <div class="fill">
        <div class="container">
          <a class="brand" href="#">Belyn</a>
          <ul class="nav">
            <li><a href="${request.route_url('dashboard')}">Глагне</a></li>
            <li><a href="#">Монитор</a></li>
            <li><a href="#">Часы</a></li>
            <li><a href="#">Слайдшоу</a></li>
            <li><a href="${request.route_url('player')}">Плеер</a></li>
            <li><a href="${request.route_url('downloader')}">Качалка</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container">
      %if request.session.peek_flash():
      <div class="alert-message warning">
        <% flash =  request.session.pop_flash() %>
        %for message in flash:
        <p>${message}</p>
        %endfor
      </div>
      %endif
      <div class="content"> 
        ${next.body()}
      </div> 
    </div>
  </body>
</html>
