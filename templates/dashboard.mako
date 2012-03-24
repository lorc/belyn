# -*- coding: utf-8 -*-
<%inherit file="layout.mako"/>

<div class="page-header">
  <h1>Dashboard</h1>
</div>
<div class="row">
  <div class="span10">
    Time now is ${time}
  </div>
</div>
%if lamps:
<div class="row">
  <div class="span10">
    <h1>
    Свет сейчас: 
    %if lamp_state!=0:
    горит
    %else:
    погашен
    %endif
    </h1>
  </div>
</div>
<div class="row">
  <div class="span10">
    %for lamp in lamps:
    <a href="${request.route_url('lights_cmd',idx=lamp.idx,cmd='toggle')}">
        %if lamp.state:
        <img src="/static/lamp_on.jpg">
        %else:
        <img src="static/lamp_off.jpg">
        %endif
    </a>
    %endfor
  </div>
</div>
<div class="row">
  <div class="span10">
    <a class="btn" href="${request.route_url('lights_cmd',idx=-1,cmd='toggle')}">
    %if lamp_state!=0:
    Выключить
    %else:
    Включить
    %endif
    </a>
    <br>
  </div>
</div>
%endif
