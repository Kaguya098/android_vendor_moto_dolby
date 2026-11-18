#!/usr/bin/env python3
"""Merge efek Dolby ke audio_effects.xml. Idempotent.  usage: patch_audio_effects.py <audio_effects.xml>"""
import sys, xml.etree.ElementTree as ET
p = sys.argv[1]
t = ET.parse(p); r = t.getroot()
libs = [("dap","libswdap.so"),("dvl","libdlbvol.so"),("gamedap","libswgamedap.so"),("vqe","libswvqe.so")]
effs = [("dap","dap","9d4921da-8225-4f29-aefa-39537a04bcaa"),
 ("dlb_music_listener","dvl","40f66c8b-5aa5-4345-8919-53ec431aaa98"),
 ("dlb_ring_listener","dvl","21d14087-558a-4f21-94a9-5002dce64bce"),
 ("dlb_alarm_listener","dvl","6aff229c-30c6-4cc8-9957-dbfe5c1bd7f6"),
 ("dlb_system_listener","dvl","874db4d8-051d-4b7b-bd95-a3bebc837e9e"),
 ("dlb_notification_listener","dvl","1f0091e3-6ad8-40fe-9b09-5948f9a26e7e"),
 ("gamedap","gamedap","3783c334-d3a0-4d13-874f-0032e5fb80e2"),
 ("vqe","vqe","64a0f614-7fa4-48b8-b081-d59dc954616f")]
streams = {"music":"dlb_music_listener","ring":"dlb_ring_listener","alarm":"dlb_alarm_listener",
           "system":"dlb_system_listener","notification":"dlb_notification_listener"}
def sec(tag):
    e = r.find(tag)
    if e is None: e = ET.SubElement(r, tag)
    return e
L, E, P = sec("libraries"), sec("effects"), sec("postprocess")
have = {x.get("name") for x in L}
for n,f in libs:
    if n not in have: ET.SubElement(L,"library",name=n,path=f)
have = {x.get("name") for x in E if x.tag=="effect"}
for n,l,u in effs:
    if n not in have: ET.SubElement(E,"effect",name=n,library=l,uuid=u)
for st,ef in streams.items():
    s = next((x for x in P if x.tag=="stream" and x.get("type")==st), None)
    if s is None: s = ET.SubElement(P,"stream",type=st)
    if not any(a.get("effect")==ef for a in s): ET.SubElement(s,"apply",effect=ef)
ET.indent(t, space="    ")
t.write(p, encoding="utf-8", xml_declaration=True)
print("patched", p)
