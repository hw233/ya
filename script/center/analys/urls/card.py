#coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #**********新手卡管理*********************************#
    url(r'^list', 'analys.views.card.card.card_list'),
    url(r'^list/', 'analys.views.card.card.card_list'),
    url(r'^log/list', 'analys.views.card.card.card_log_list'),
    url(r'^log/list/', 'analys.views.card.card.card_log_list'),
    url(r'^log/recover/', 'analys.views.card.card.card_log_recover'),
    url(r'^log/recover', 'analys.views.card.card.card_log_recover'),
    url(r'^(\d+)$', 'analys.views.card.card.card'),
    url(r'^create', 'analys.views.card.card.card_create'),
    url(r'^create/', 'analys.views.card.card.card_create'),
    url(r'^del', 'analys.views.card.card.card_del'),
    url(r'^del/', 'analys.views.card.card.card_del'),
    url(r'^get/(\d+)/(\d+)$', 'analys.views.card.card.card_get'),
    url(r'^get/(\d+)$', 'analys.views.card.card.card_get'),
    url(r'^get/$', 'analys.views.card.card.card_get'),
    url(r'^use', 'analys.views.card.card.card_use'),
    url(r'^batch$', 'analys.views.card.batch.batch_list'),
    url(r'^batch/$', 'analys.views.card.batch.batch_list'),
    url(r'^batch/edit', 'analys.views.card.batch.batch_edit'),
    url(r'^batch/edit/', 'analys.views.card.batch.batch_edit'),
    url(r'^batch/save', 'analys.views.card.batch.batch_save'),
    url(r'^batch/save/', 'analys.views.card.batch.batch_save'),
    url(r'^batch/del', 'analys.views.card.batch.batch_del'),
    
    url(r'^batch/del/', 'analys.views.card.batch.batch_del'),
    url(r'^batch/recover', 'analys.views.card.batch.batch_recover'),
    url(r'^batch/recover/', 'analys.views.card.batch.batch_recover'),
    url(r'^batch/group/ajax', 'analys.views.card.batch.group_ajax'),
    url(r'^batch/group/ajax/', 'analys.views.card.batch.group_ajax'),
    url(r'^export', 'analys.views.card.card.export_card'),
    url(r'^export/', 'analys.views.card.card.export_card'),

    url(r'^prize$', 'analys.views.card.prize.prize_list'),
    url(r'^prize/list$', 'analys.views.card.prize.prize_list'),
    url(r'^prize/list/$', 'analys.views.card.prize.prize_list'),
    url(r'^prize/$', 'analys.views.card.prize.prize_list'),
    url(r'^prize/edit', 'analys.views.card.prize.prize_edit'),
    url(r'^prize/edit/', 'analys.views.card.prize.prize_edit'),
    url(r'^prize/save', 'analys.views.card.prize.prize_save'),
    url(r'^prize/save/', 'analys.views.card.prize.prize_save'),
    url(r'^prize/del', 'analys.views.card.prize.prize_del'),
    url(r'^prize/del/', 'analys.views.card.prize.prize_del'),
    url(r'^prize/recover', 'analys.views.card.prize.prize_recover'),
    url(r'^prize/recover/', 'analys.views.card.prize.prize_recover'),
)
