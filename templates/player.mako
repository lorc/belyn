# -*- coding: utf-8 -*-
<%inherit file="layout.mako"/>

<div class="page-header">
  <h1>Плеер</h1>
</div>
<div class="row">
  <div class="span16">
    <form method="POST">
      <fieldset>
        <div class="clearfix">
          <label for="file">Что</label>&nbsp
            <input id="file" name="file" type="text" size="50"/>
          <input type="submit" class="btn primary" value="Играть">
        </div>
      </fieldset>
    </form>
  </div>
</div>
<div class="row show-grid">
  <div class="span4">
    <h1>Управление плеером</h1>
  </div>
  <div class="span12">
    <a class="btn" href="${request.route_url('player_cmd',cmd='pause')}">Пауза</a>
    <a class="btn" href="${request.route_url('player_cmd',cmd='seek_left')}">&#8592;</a>
    <a class="btn" href="${request.route_url('player_cmd',cmd='seek_right')}">&#8594;</a>
    <a class="btn" href="${request.route_url('player_cmd',cmd='stop')}">Стоп</a>
    <a class="btn" href="${request.route_url('player_cmd',cmd='ch_sub')}">Переключить субтирты</a>
    <a class="btn" href="${request.route_url('player_cmd',cmd='ch_snd')}">Переключить звук</a>
  </div>
</div>
