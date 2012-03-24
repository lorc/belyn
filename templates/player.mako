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
<div class="row">
  <div class="span4">
    <h2>Управление плеером</h2>
  </div>
  <div class="span12">
    <div class="row">
      <div class="span4">
        <h3>Воспроизведение</h3>
      </div>
      <div class="span8">
        <a class="btn" href="${request.route_url('player_cmd',cmd='pause')}"  onclick="post_control('pause');return false;"> Пауза</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='seek_left')}" onclick="post_control('seek_left');return false;">&#8592;</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='seek_right')}" onclick="post_control('seek_right');return false;">&#8594;</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='stop')}" onclick="post_control('stop');return false;">Стоп</a>
      </div>
    </div>
    <div class="row">
      <div class="span4">
        <h3>Звук</h3>
      </div>
      <div class="span8">
        <a class="btn" href="${request.route_url('player_cmd',cmd='snd_change')}">Переключить дорожку</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='snd_mute')}">Выключить</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='snd_up')}">Громче</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='snd_down')}">Тише</a>
      </div>
    </div>
    <div class="row">
      <div class="span4">
        <h3>Субтитры</h3>
      </div>
      <div class="span8">
        <a class="btn" href="${request.route_url('player_cmd',cmd='ch_sub')}">Переключить</a>
        <a class="btn" href="${request.route_url('player_cmd',cmd='ch_snd')}">Выключить</a>
      </div>
    </div>
  </div>
</div>
%if media:
<hr/>
<div class="row">
  <div class="span4">
    <h2>Библиотека</h2>
  </div>
  <div class="span12">
    %for m in media:
    <div class="folder" style="border:1px solid gray;margin-bottom:5px">
      <div class="head" >
        <h4><a href="#" onclick="$(this).parent().parent().next().toggle('fast');return false;">${m[0][10:]}</a></h4>
      </div>
      <div class="files" style="display:none;" >
        %for file in m[1]:
        <a href="#" onclick="post_file('${m[0]}/${file}')">${file}<br></a>
        %endfor
      </div>
    </div>
    %endfor
  </div>
</div>
<script type="text/javascript">
function post_control(cmd)
{
    $.ajax({url:"${request.route_url('player')}/"+cmd,
            success: function (data) {
//                if (data.error != "")
//                {
//                    alert("Json call error:" + data.error)
//                }
            }
           })
}
function post_file(file) {
    method ="post"; 

    var form = document.createElement("form");
    form.setAttribute("method", method);
   // form.setAttribute("action", path);

   var hiddenField = document.createElement("input");
   hiddenField.setAttribute("type", "hidden");
   hiddenField.setAttribute("name", "file" );
   hiddenField.setAttribute("value", file);
   form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}
</script>
%endif
