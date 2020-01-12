{% extends 'head.html' %}
{% load staticfiles %}
{% block paginator %}
{% if images %}
{% if paginator.visible %}
<div class="container"><center><ul class="pagination">
{% if paginator.big %}{% if paginator.active_page == 1 %}<li class="disabled"><a href="#">&laquo;&laquo;</a></li>{% else %}<li><a href="/cam/grid/{{ active_tab }}/1/">&laquo;&laquo;</a></li>{% endif %}{% endif %}
{% if paginator.active_page == 1 %}<li class="disabled"><a href="#">&laquo;</a></li>{% else %}<li><a href="/cam/grid/{{ active_tab }}/{{ paginator.active_page|add:"-1" }}/">&laquo;</a></li>{% endif %}
 {% for page in paginator.pages %}
 {% if page == 0 %}<li class="disabled"><a href="/cam/grid/{{ active_tab }}/{{ paginator.active_page }}/">...</a></li>
 {% elif paginator.active_page == page %}<li class="active"><a href="/cam/grid/{{ active_tab }}/{{ page }}/">{{ page }}</a></li>
 {% else %}<li><a href="/cam/grid/{{ active_tab }}/{{ page }}/">{{ page }}</a></li>{% endif %}{% endfor %}
{% if paginator.active_page == paginator.pagecount %}<li class="disabled"><a href="#">&raquo;</a></li>{% else %}<li><a href="/cam/grid/{{ active_tab }}/{{ paginator.active_page|add:"1" }}/">&raquo;</a></li>{% endif %}
{% if paginator.big %}{% if paginator.active_page == paginator.pagecount %}<li class="disabled"><a href="#">&raquo;&raquo;</a></li>{% else %}<li><a href="/cam/grid/{{ active_tab }}/{{ paginator.pagecount }}/">&raquo;&raquo;</a></li>{% endif %}{% endif %}
</ul></center></div>
{% else %}
<div class="container-fluid" style="margin-top: 10px;"></div>
{% endif %}
{% endif %}
{% endblock %}

{% block javascript %}{% if images %}<script>
document.onkeydown = function(evt) { evt = evt || window.event; switch (evt.keyCode) {
 case 37: if ({{ paginator.active_page}} > 1) {
  window.location = "http://www.kuvalda.lv/cam/grid/{{ active_tab }}/{{ paginator.active_page|add:"-1" }}/"; } break;
 case 39: if ({{ paginator.active_page }} < {{ paginator.pagecount }}) {
  window.location = "http://www.kuvalda.lv/cam/grid/{{ active_tab }}/{{ paginator.active_page|add:"1" }}/"; } break; }};
</script>{% endif %}{% endblock %}

{% block style %}
.pagination { margin-top: 10px; margin-bottom: 5px; }
ul.pagination li a:hover:not(.active) {background-color: #ddd;}
.nav-tabs > li > a{ color: #000; background-color:#eee; }
.nav-tabs > li > a:hover{ background-color: #ccc !important; color:#fff; }

#grid_img{ position: relative; width: 202px; height: 152px;
/* padding: 0px 0px 0px 0px; */
 margin: 1px 1px 1px 1px; border: 1px #ccc; float:left; }

#del_button{ position:absolute; width:25px; height:25px; right:0px; bottom:0px; 
margin-top:26px; margin-right:3px; z-index:1; }
#share_button{ position:absolute; width:25px; height:25px; right:0px; top:0px; margin-top:26px; margin-right:29px; z-index:1; border: 1px solid red; }
p{ position:absolute; width:100%; height:100%; top:0; left: 0; z-index: 0; background-image: url( {% static 'empty.png' %} ); }

{% endblock %}
