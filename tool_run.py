try:
    import sys
    RESET='S'
    if RESET=='Y' or RESET=='y':
        RESET=True
    else:
        RESET=False
except:
    RESET=False
if RESET:
    import shutil
    LIST=['./Pmin_Sources','com.garena.game.kgvn','dance.xml','organSkin.bytes','File_Mod']
    for i in LIST:
        try:
            shutil.rmtree(i)
        except:
            pass
else:
    import os
    from zipfile import ZipFile
    # Tải và giải nén từng file
    import os
    try:import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style;from termcolor import colored
    except:
        try:os.system('python -m pip install pyzstd');os.system('python -m pip install termcolor');os.system('python -m pip install colorama');os.system('python -m pip install bs4');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
        except:os.system('pip install pyzstd');os.system('pip install termcolor');os.system('pip install colorama');os.system('pip install bs4');import pyzstd;from colorama import Fore;from colorama import Fore;from colorama import Style;from colorama import Style
    from shutil import make_archive;from pyzstd import decompress,compress,ZstdDict;from os import listdir;import sys;import os;from termcolor import colored;import re;import getopt;import pyzstd;import sys;import glob;import colorama;from colorama import Fore;from colorama import Style;from colorama import Fore;from colorama import Style;import shutil;import zipfile;import shutil;from zipfile import* 
    import xml.etree.ElementTree as ET
    import sys
    from xml.dom import minidom
    import random
    ZSTD_DICT=b'7\xa40\xec\xe7UC\x0bM\x10@\xae\xa6\xe9P\xaa\xffPL\x8d\xe1Tn)\xb7Dr\xbb\xecH\xaclT)(((((\xa0\xa2\xa0CU(G\x01\x18\x08r\x18\x11\x11\x9a]k\xd3\x8a:\x16\xa9\x89\xe8%\xc2\xde{\xef\xbd\xa5\x8e\xae\xdb2\xaa\x8ee\x99\x85a\xf0\xf9\xf1#\x9b\x02\x83\x05\x19\x0c\x08\x06\x05b\xa1`\x96\xc6\x81\xac}\x04D\xe4\xe1\xa4\xc3\x01\xe2`A\xc1\xe0`\xc1\xa0\xc0\xa0`0\x10\x08\x03\xc3\xc0@(\x10\x06\x80\xc2\xc2@ \x1c\n\x07D\x82\xf48\xe9\x96\x1b\x00\xd4\x0e\x11\x06\x1d\x8bA\x901\xc6\x18bH\x19\x00 \x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x08\x00\x00\x00mName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="skillCombineLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="skillCombineSrcId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSkillMark" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration14" eventType="HitTriggerDuration" guid="38f874e2-e64b-478d-be55-fc7453046e1c" enabled="true" refParamName="" useRefParam="false" r="0.183" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="8" guid="1b06b263-6aa9-4007-a2cb-116a920b9312" status="true"/>\n\t\t\t<Event eventName="HitTriggerDuration" time="0.200" lenid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack0" eventType="StopTrack" guid="8013dc81-a485-4567-bc08-9e0ec7d7cd99" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.017" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="4" guid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack1" eventType="StopTrack" guid="8633109d-53e5-4931-87b1-bf3472773aed" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.633" exe\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe8\xb0\xa6\xe8\xae\xa9"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe6\x94\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x87\xaa\xe6\x9d\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe9\x99\xa4\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="Buff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x81\xa2\xe5\xa4\x8dBuff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe5\xb0\x84\xe7\xa8\x8b"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="CheckSkillCombineConditionTick1" eventType="CheckSkillCombineConditionTick" guid="bc7f4540-c6d9-4813-88cb-990e1d8abf7f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.433" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentBuffId" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="skillCombineId" value="136001" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType"ame="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidMoveButRotate" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<int name="rotateSpeed" value="720" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t</Event>\r\n\t\t</Track>\r\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="4abae504-d3a2-4370-a0a8-255fde6c84d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true" />\r\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="0.500" isDuration="true">\r\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<String name="clipName" value="Hit" refP/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00\xbb\x01\x00\x00J\x00\x00\x00\x17\x00\x00\x00Terms_Of_Service_Title\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x1c\x00\x00\x00\xc4\x90i\xe1\xbb\x81u kho\xe1\xba\xa3n d\xe1\xbb\x8bch v\xe1\xbb\xa5\x00=\x00\x00\x00\xe0\xb9\x80\xe0\xb8\x87\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\x82\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\x00\x11\x00\x00\x00\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4 \xec\x95\xbd\xea\xb4\x80\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x12\x00\x00\x00Ketentuan Layanan\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe5\x88\xa9\xe7\x94\xa8\xe8\xa6\x8f\xe7\xb4\x84\x00g\x13\x00\x00K\x00\x00\x00\x16\x00\x00\x00Terms_Of_Service_Text\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\xe5\x85\xa7\xe5\xae\xb9\xe5\x85\xa7\xe5\xae\xb9\xe5\xbc\x89"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="collisionCheckDistanceOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="collisionCheckWidth" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInteruptOtherMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bProtectInteruptedByOtherMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsAreaLimitedToBeMoveDone" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="d7e3a6f9-943b-4dda-9650-7a88a29698f8" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.783" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnObjectDuration" time="0.233" length="0.300" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="parentId" ob\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00^KL\x00\x14\x00\x00\x000AF0A00F2605E9BB_##\x00\x00\x00\x14\x00\x00\x00349C21E70FD859FE_##\x00\x01\x00\x00\x00\x00\xe7.\x00\x00\x01\x00\x00\x00\x00\x04\x04\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00\x90\x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\n\x00\x00\x00}\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa0\x00\x00\x00\x00\xbc\x96\x98J\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00`KL\x00\x14\x00\x00\x00B8FA881B79F41C0F_##\x00\x00\x00\x14\x00\x00\x0085F89A39568DD08B_##\x00\x01\x00\x00\x00\x00`KL\x00\x01\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00b\x00\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0f\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x01\x00\x00_KL\x00\x14\x00\x00\x004BF61216E72F555D_##\x00\x00\x00\x14\x00\x00\x00EA1631C678E20D11_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00starguardcard.png\x00\x04\x16\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x002\x00\x00\x00\xfa\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x80A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x01\x00\x00@\x85:\xe1\\\x12\x00\x00@\xeb<\r\xa5\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00\x05^\x0c\x00\x14\x00\x00\x00DEC1050D07839DB7_##\x00\x00\x00\x14\x00\x00\x00F620F03B6DE88773_##\x00\x01\x00\x00\x00\x00\xfa\x97\x04\x00\x01\x00\x00\x00\x00\x04\n\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00 \x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\xa4\x04\x00\x00 \x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x00\x00\xd2B\x00\x00\x80?\x00\x00\x00\x00\x00\x00\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\x87\xb4\xe5\x91\xbd\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe7\xa6\x81\xe7\x94\xa8\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe8\x83\xbd\xe9\x87\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\xa4\xe7\x94\xb2\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb\xe5\xb8\xa6\xe6\xb3\x95\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2\xef\xbc\x88\xe7\xa6\x81\xe6\xad\xa2\xe4\xbd\xbf\xe7\x94\xa8\xef\xbc\x89"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x83\xbd\xe9\x87\x8f\xe5\x8d\xe7\xba\xbf\xe5\x8e\x8b\xe5\x8a\x9b\xef\xbc\x9b\\n\\n\xe2\x80\xa6\xe2\x80\xa6\\n\\n\xe4\xba\xba\xe7\xb1\xbb\xe7\x9a\x84\xe5\xbc\xba\xe8\x80\x85\xe4\xbb\xac\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe5\x90\x84\xe8\x87\xaa\xe4\xb8\xba\xe6\x88\x98\xe7\x9a\x84\xe6\x97\xa5\xe5\xad\x90\xef\xbc\x8c\xe4\xbb\x96\xe4\xbb\xac\xe8\x81\x9a\xe9\x9b\x86\xe5\x9c\xa8\xe8\x90\xa8\xe5\xb0\xbc\xe7\x9a\x84\xe9\xba\xbe\xe4\xb8\x8b\xef\xbc\x8c\xe5\xb0\x86\xe4\xb8\x80\xe8\x82\xa1\xe8\x82\xa1\xe5\xbe\xae\xe5\xb0\x8f\xe7\x9a\x84\xe5\x8a\x9b\xe9\x87\x8f\xef\xbc\x8c\xe8\x81\x9a\xe5\x90\x88\xe6\x88\x90\xe6\x8e\xa8\xe5\x8a\xa8\xe5\x8e\x86\xe5\x8f\xb2\xe7\x9a\x84\xe6\xb4\xaa\xe6\xb5\x81\xe3\x80\x82\xe5\x9c\xa8\xe8\xbf\x99\xe8\x82\xa1\xe6\xb4\xaa\xe6\xb5\x81\xe9\x9d\xa2\xe5\x89\x8d\xef\xbc\x8c\xe5\xbc\xba\xe5\xa4\xa7\xe7\x9a\x84\xe6\x81\xb6\xe9\xad\x94\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x80\xe5\xae\x88\xe6\xb7\xb1\xe6\xb8\x8a\xef\xbc\x8c\xe7\x8b\x82\xe9\x87\x8e\xe7\x9a\x84\xe5\x85\xbd\xe7\xbe\xa4\xe5\xad\xa6\xe4\xbc\x9a\xe4\xba\x86\xe8\x87\xaa\xe6\x88\x91\xe6\x94\xb6\xe6\x95\x9b\xef\xbc\x8c\xe5\xb0\xb1\xe8\xbf\x9e\xe5\x9c\xa3\xe6\xae\xbf\xe7\x9a\x84\xe7\xa5\x9e\xe7\xa5\x87\xe4\xbb\xac\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe7\x9b\xb4\xe6\x8e\xa0\xe9\x94\x8b\xe8\x8a\x92\xe3\x80\x82\xe4\xbd\x86\xe8\x90\xa8\xe5\xb0\xbc\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa2\xab\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe5\x8a\x9f\xe7\xbb\xa9\xe5\x86\xb2\xe6\x98\x8f\xe5\xa4\xb4\xe8\x84\x91\xef\xbc\x8c\xe4\xbb\x96\xe6\x97\xb6\xe5\x88\xbb\xe4\xbf\x9d\xe6\x8c\x81\xe7\x9d\x80\xe8\xad\xa6\xe6\x83\x95\xef\xbc\x8c\xe5\x8f\xaa\xe8\xa6\x81\xe6\x88\x98\xe6\x96\x97\xe7\x9a\x84\xe5\x8f\xb7\xe8\xa7\x92\xe5\x90\xb9\xe5\x93\x8d\xef\xbc\x8c\xe4\xbb\x96\xe5\xb0\xb1\xe4\xbc\x9a\xe5\x86\x8d\xe6\xac\xa1\xe6\x8c\xba\xe5\x89\x91\xe8\x80\x8c\xe4\xb8\x8a\xe3\x80\x82\\n\\n\xe2\x80\x9c\xe5\x90\xbe\xe6\x89\xa7\xe5\x90\xbe\xe5\x89\x91\xef\xbc\x8c\xe6\x96\xa9\xe5\xb0\xbd\xe5\xa5\xb8\xe9\x82\xaa\xef\xbc\x81\xe2\x80\x9d\r\n0588A320CABA3789_## = \xe7\x81\xb5\xe7\x81\xb5\xe4\xb8\xba\xe4\xbb\x80\xe4\xb9\x88\xe6\x98\xaf\xe7\x88\x86\xe7\x82\xb8\xe5\xa4\xb4\xef\xbc\x9f\r\n0590EDDF3CC30F2A_## = \xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\xba\xef\xbc\x8c\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\x9a\xe6\x84\x8f\xe6\x89\x93\xe5\x8a\xa8\xe4\xba\x86\xe6\x88\x91\\n\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe4\xb8\x8d\xe4\xbb\x8b\xe6\x84\x8f\xe5\x92\x8c\xe6\x88\x91\xe4\xb8\x80\xe8\xb5\xb7\\n\xe8\xa1\x8c\xe4\xbe\xa0\xe6\xad\xa3\xe4\xb9\x89\xef\xbc\x8c\xe9\x99\xa4\xe6\x81\xb6\xe6\x89\xac\xe5\x96\x84\\n\xe5\x88\x9a\xe5\xa5\xbd\xe6\x88\x91\xe7\x8e\xb0\xe5\x9c\xa8\xe7\xbc\xba\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa9\xe7\x90\x86\\n\xe4\xbb\x8a\xe5\x90\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\xb1\xe6\x98\xaf\xe6\x97\xa0\xe6\x95\x8c\xe7\x9a\x84\xe9\x9c\xb9\xe9\x9b\xb3\xe7\xbb\x84\xe5\x90\x88\xef\xbc\x81\r\n0592D198A67E021F_## = <color=#ffd200>\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6</color>\xef\xbc\x9a\xe4\xb8\x8e<color=#ffd200>{0}</color>\xe8\xbe\xbe\xe5\x88\xb0<color=#ffd200>\xe7\xbe\x81\xe7\xbb\x8a\xe9\x98\xb6\xe6\xae\xb52 \xe7\x9b\xb8\xe8\xaf\x86</color>\r\n05A181D7672725DC_## = \xe6\xb4\x9b\xe9\x87\x8c\xe6\x98\x82\r\n05A9BBD41D0A9179_## = \xe2\x80\x9c\xe4\xb9\x9d\xe5\xa4\xa9\xe4\xb9\x8b\xe4\xb8\x8a\xef\xbc\x8c\xe7\xa5\x9e\xe5\xba\xa7\xe4\xb9\x8b\xe6\x97\x81\xef\xbc\x8c\xe5\x85\xad\xe7\xbf\xbc\xe8\x88\x9e\xe5\x8a\xa8\xef\xbc\x8c\xe4\xbb\xa5\xe7\xbf\xb1\xe4\xbb\xa5\xe7\xbf\x94\xe3\x80\x82\xe2\x80\x9d\\n\\n\xe8\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x97\x8b\xe8\xbd\xac"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="materialParentActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyScaling" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableLayer"head145.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x15\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00:\x00\x00\x00\x0f\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\xf6\x99\x00\x0c\x00\x00\x00vp10042.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00X\x00\x00\x00\x0f\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x17\xf6\x99\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x18\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x01\x00\x00\x00\x00O\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00\xab\x9e\x98\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x19\xf6\x99\x00\x12\x00\x00\x00return_js_new.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1a\xf6\x99\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1b\xf6\x99\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1c\xf6\x99\x00\x0c\x00\x00\x00vp90007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1d\xf6\x99\x00\x0c\x00\x00\x00vp10106.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00>\x00\x00\x00\x0f\x00\x00\x00\x0f\x00\x00\x00\xac\x9e\x98\x00\x0c\x00\x00\x00vp90005.png\x00\x1e\xf6\x99\x00\x10\x00\x00\x00valorpass03.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1f\xf6\x99\x00\x0c\x00\x00\x00vp12007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00 \xf6\x99\x00\x0c\x00\x00\x00vp11029.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00!\xf6\x99\x00\r\x00\x00\x00vp120100.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00Q\x00\x00\x00\x0f\x00\x00\x00\x14\x00\x00\x00\xad\x9e\x98\x00\x0c\x00\x00\x00vp90007.png\x00#\xf6\x99\x00\x14\x00\x00\x00level20skin_big.png\x00\x01\x00\x00\x00\x00\x10\x00\x00\x00level20skin.png\x00;\x00\x00\x00\x0f\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\xe7\x8e\x84\xe7\xad\x96\xe8\xa2\xab\xe5\x8a\xa8\x00\x16\x00\x00\x00\xe5\x87\xbb\xe6\x9d\x80\xe6\x88\x96\xe5\x8a\xa9\xe6\x94\xbb\xe8\x8b\xb1\xe9\x9b\x84\x007\x00\x00\x00Prefab_Characters/Prefab_Hero/195_BaiLiXuanCe/skill/P2\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00(<\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\xe5\x8f\xb6\xe5\xa8\x9c\xe5\xad\xa6\xe4\xb9\xa0\xe5\xa4\xa7\xe6\x8b\x9b\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x004\x00\x00\x00Prefab_Characters/Prefab_Hero/154_HuaMuLan/skill/P1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xce\x00\x00\x00%\xd5\x01\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00[EX]\xe7\x99\xbd\xe8\xb5\xb7\xe8\xa2\xab\xe5\x8a\xa8\x00\x13\x00\x00\x00\xe5\x8f\x97\xe5\x87\xbb\xe6\x9c\x89\xe5\x87\xa0\xe7\x8e\x87\xe8\xbd\xac\x00:\x00\x00\x00Prefab_Characters/Prefab_Hero/120_BaiQi/skill/extend/exP1\x00\x02\x00\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\xbf\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xe7\xba\xb3\xe5\x85\x8b\xe7\xbd\x97\xe6\x96\xaf\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/150_HanXin/skill/extend/exP2\x00\x08\x00\x00\x00\xa0\x0f\x00\x00\x14\x00\x00\x00\xf4\x01\x00\x00\x8c\x06\x17\x00\x98:\x00\x00\x0c\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x12\x01\x00\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00\xef\xbc\x8810v10\xef\xbc\x89\xe7\x8c\xb4\xe5\xad\x90\xe6\xaf\x8f\xe6\xac\xa1\xe9\x87\x8a\xe6\x94\xbe\xe6\x8a\x80\xe8\x83\xbd\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xe5\xb0\x86\xe4\xbc\x9a\xe8\x8e\xb7\xe5\xbe\x97\xe4\xb8\x80\xe4\xb8\xaa\xe6\x8a\xa4\xe7\x9b\xbe\xef\xbc\x8c\xe5\x8f\xaf\xe5\x8f\xa0\xe5\x8a\xa05\xe6\xac\xa1\x00\x12\x00\x00\x00\xe6\x82\x9f\xe7\xa9\xba[EX]\xe8\xa2\xab\xe5\x8a\xa81\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/167_WuKong/skill/extend/exP1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00e="" r="0.517" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CameraShakeDuration" time="2.000" length="2.000" isDuration="true">\n\t\t\t\t<bool name="useMainCamera" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="shakeRange" x="0.500" y="0.500" z="0.500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_self" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_target" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_enemy" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_allies" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useAccumOffset" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cosDecay" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="cosDecayFactor" v\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00M\x00\x00\x00\x1f\xb2\x01\x00%\x00\x00\x00Play_SunShangXiang_VO_TiaoXin_Skin13\x00i+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00J\x00\x00\x00)\xb2\x01\x00"\x00\x00\x00Play_sunshangxiang_tiaoxin_Skin14\x00j+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00\x85\xb5\x01\x00\x18\x00\x00\x00Play_GongShuBan_TiaoXin\x00\xc0+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\x99\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin2\x00\xc2+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xb7\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin5\x00\xc5+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xc1\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin6\x00\xc6+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00m\xb9\x01\x00\x18\x00\x00\x00Play_ZhuangZhou_TiaoXin\x00$,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00=\x00\x00\x00U\xbd\x01\x00\x15\x00\x00\x00Play_LiuShan_TiaoXin\x00\x88,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00?\x00\x00\x00=\xc1\x01\x00\x17\x00\x00\x00Play_GaoJianLi_TiaoXin\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00Q\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin2\x00\xee,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00[\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin3\x00\xef,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00<\x00\x00\x00%\xc5\x01\x00\x14\x00\x00\x00Play_JingKe_TiaoXin\x00P-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00M\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin4\x00T-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00W\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin5\x00U-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00C\x00\x00\x00o\xc6\x01\x00\x1b\x00\x00\x00Plname="bInverse" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupActorType" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupRadius" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterInTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="teamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="diffTeamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="monsterTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="soldierTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetBehaviourModeTick0" eventType="SetBehaviourModeTick" guid="53e062a5-ebd1-4b49-83fe-4b2026e48ae4" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.283" exe\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bChargingEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="chargingDistance" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="distance" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bResetMoveDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="minSpeed" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="12000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groundOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreHeight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="acceleration"v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/skill1_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_organ/tower/skill1_bullet_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/makeDamage2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00*\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc3\x00\x00\x00\x02\x00\x00\x00r\x00\x00\x00\x06\x00\x00\x00v1`\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String2\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/A1E2\x04\x00\x00\x00\x04\x00er/New_BlueTower/skill/New_BlueTower_makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00L\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe5\x00\x00\x00\x02\x00\x00\x00\x94\x00\x00\x00\x06\x00\x00\x00v1\x82\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringT\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_BlueTower/skill/New_BlueTower_A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75001\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xad\x03\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x1d\x03\x00\x00\x03\x00\x00\x00\x07\x01\x00\x01\x00\x00\x00\x00\x00\r\x00\x00\x00\xe5\xa4\xa7\xe7\xa5\x9e\xe5\x85\xb3\xe5\x8d\xa1\x00\x15\x00\x00\x00Tutorial_BGod_Design\x00\x17\x00\x00\x00ART_5V5_01_High_Artist\x00\x0c\x00\x00\x00PVP_5V5_Nav\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00~\x02\x00\x00z\x02\x00\x00{\x02\x00\x00\x7f\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x02\x00\x00w\x02\x00\x00x\x02\x00\x00\x80\x02\x00\x00\x81\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x007\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x08\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x00\x00pvp_5_small\x00\r\x00\x00\x00pvp_5_detail\x00\n\x00\x00\x00pvp_5_big\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xdd\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x02\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00Play_PVP_Music\x00\x0f\x00\x00\x00Stop_PVP_Music\x00\x01\x00\x00\x00\x00\n\x00\x00\x00Music_PVP\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90_\x01\x00\x95_\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x02\x00\x00e\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x10\x00\x00\x00\xe5\x8f\xac\xe5\x94\xa4\xe5\xb8\x88\xe6\x88\x98\xe5\x9c\xba\x00\x15\x00\x00\x00PVE_1_1_logic_Design\x00\x18\x00\x00\x00ART_PJGC_02_High_Artist\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00Img_Story\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x03\x00\x00\x00\xf3\x03\x00\x00\xf4\x03\x00\x00\xf5\x03\x00\x00Q\xc3\x00\x00\x00\x00\x00\x00f\x00\x00\x00\x05M\x04\x00\x00\x05\xb1\x04\x00\x00\x05\x15\x05\x00\x00\x05{\x05\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\t\x00\x00\x00\r\x00\x00\x00F\x05\x00\x00\xe7\x06\x00\x00\x88\x08\x00\x00\x9e\t\x00\x00\x84\x03\x00\x00\x9a\x04\x00\x00\xb0\x05\x00\x00i\x06\x00\x00\x00\x08\x00\x00\x00PVE_1_3\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa*\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00o\x00\x00\x00y\x00\x00\x00\x83\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\x0ee\x00\x01\x00\x00\x00\x00E\x00\x00\x00f\x82\x17\x00\x19\x00\x00\x00Play_Yena_VOX_Come_Skin7\x00/<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00@\x00\x00\x00\xba\xa6\x17\x00\x14\x00\x00\x00Play_LuoBin_VO_Come\x00\x8c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00D\x00\x00\x00\xca\xcd\x17\x00\x18\x00\x00\x00Play_ZhangLiang_VO_Come\x00\xf0<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00\xf6\xce\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin3\x00\xf3<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00Z\xcf\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin4\x00\xf4<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00A\x00\x00\x00\xda\xf4\x17\x00\x15\x00\x00\x00Play_BuZhiHuoWu_Show\x00T=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\x06\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin3\x00W=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00j\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin4\x00X=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\xce\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin5\x00Y=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x002\xf7\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin6\x00Z=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00)\x00\x00\x00\xea\x1b\x18\x00\x01\x00\x00\x00\x00\xb8=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00)\x00\x00\x00\nj\x18\x00\x01\x00\x00\x00\x00\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00*\xb8\x18\x00\x16\x00\x00\x00Play_Nakelulu_VO_Come\x00H?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00V\xb9\x18\x00\x1c\x00\x00\x00Play_Nakelulu_VO_Come_Skin3\x00K?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00:\xdf\x18\x00\x1c\x00\x00\x00Play_163_JuYouJing_VOX_Come\x00\xac?\x00\x01\x00\x00\x00\x00\x00?\x00\x00\x00Prefab_Skill_Effects/Level_Effects/AutoChess_Effects/ChessDrop\x00\x00\x00\x80?\x01\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MSES\x07\x00\x00\x00\x17\x00\x00\x00\x0f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005d388e873657b33c203ea1a6adbbd555\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x001131\x00\x02\x00\x00\x00P\x00\x13\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x001132\x00\x02\x00\x00\x00B\x00\x12\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00901\x00\x02\x00\x00\x00C\x00\x12\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00902\x00\x02\x00\x00\x00D\x00\x13\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x001130\x00\x02\x00\x00\x00E\x00\x13\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x001133\x00\x02\x00\x00\x00F\x00\x13\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x001134\x00\x02\x00\x00\x00G\x00\x13\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x001135\x00\x02\x00\x00\x00H\x00\x13\x00\x00\x00\t\x00\x00\x00\x05\x00\x00\x001136\x00\x02\x00\x00\x00I\x00\x13\x00\x00\x00\n\x00\x00\x00\x05\x00\x00\x001137\x00\x02\x00\x00\x00J\x00\x13\x00\x00\x00\x0b\x00\x00\x00\x05\x00\x00\x001138\x00\x02\x00\x00\x00K\x00\x13\x00\x00\x00\x0c\x00\x00\x00\x05\x00\x00\x001139\x00\x02\x00\x00\x00L\x00\x13\x00\x00\x00\r\x00\x00\x00\x05\x00\x00\x001180\x00\x02\x00\x00\x00M\x00\x13\x00\x00\x00\x0e\x00\x00\x00\x05\x00\x00\x001181\x00\x02\x00\x00\x00N\x00\x13\x00\x00\x00\x0f\x00\x00\x00\x05\x00\x00\x001183\x00\x02\x00\x00\x00O\x00MSES\x07\x00\x00\x00\x82\x01\x00\x00a\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e7c2b766e9bca08f64db4f0b283f3ce4\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xd6\x00\x00\x00i\x00\x00\x00\x14\x00\x00\x0096C81CC5CA834D6C_##\x00\x1f\x00\x00\x00WrapperAI/Hero/HeroAutoChessAI\x00\xa0(\x00\x00\x00\x00\x00\x00LO\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00$\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Born\x00\x01\x00\x00\x00\x00)\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Dead_Born\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x00\x00\x00j\x00\x00\x00\x14\x00\x00\x000D17FEB38CC06\x00\x00\x00\x04\x00\x00\x00&\x01\x00\x00\x12\x00\x00\x00iCollisionSize&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00x9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V500\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00z9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/542_Tachi/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/542_Tachi/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xab%\xb5\xdc\x86\x1c\x00\x00\x86\x1c\x00\x00/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81^\x00\x00\x00Prefab_Hero/542_Tachi/542_Tachi_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xdb\x00\x00\x001\x1d\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00121_MiYue/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00121_MiYue/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00121_MiYue/skill/AutoChess/PK\x03\x04RefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAlwaysLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="b1stTickParentRot" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHideWhenDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreWhenHideModel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUse3DUICamerang name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRefreshVision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidTargetOutOfNavmeshConvexHull" va\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x06\x05\x00\x00\x04\x00\x00\x00\x1e\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb7\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00F\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdf\x00\x00\x00\x02\x00\x00\x00\x8e\x00\x00\x00\x06\x00\x00\x00v1|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00M\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe6\x00\x00\x00\x02\x00\x00\x00\x95\x00\x00\x00\x06\x00\x00\x00v1\x83\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringU\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack02_spell01\x04\x00\x00P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x004EEC4F2E66D84324_##\x00\x14\x00\x00\x0022CA5E1185A20996_##\x00\n\x00\x00\x0011084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa2\x00\x00\x00\\R\x00\x00\x02\x00\x01\x01=\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/kill/Kill_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x009C5DF28AAE7D3EE2_##\x00\x14\x00\x00\x00D24D8A620C89E63A_##\x00\n\x00\x00\x0021084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa6\x00\x00\x00ly\x00\x00\x03\x00\x01\x01A\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00849FC2788990326B_##\x00\x14\x00\x00\x00E94BDB26D3AF7FEB_##\x00\n\x00\x00\x0031084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa5\x00\x00\x00M+\x00\x00\x01\x00\x01\x01@\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/returncity/return_5V5_01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00ACA13FE146E55BC7_##\x00\x14\x00\x00\x00F3CFA939C7E48289_##\x00\n\x00\x00\x0011085.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc9\x00\x00\x00*\xa0\x00\x00\x04\x00\x01\x011\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_houyi_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x009DF7DA730FC32408_##\x00\x14\x00\x00\x00559A118E1D79C256_##\x00\n\x00\x00\x0041002.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc7\x00\x00\x00+\xa0\x00\x00\x04\x00\x01\x01/\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_jin_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x0084D3846A3B38B40D_##\x00\x14\x00\x00\x00D3B4AFBD692854AB_##\x00\n\x00\x00\x0041003.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc8\x00\x00\x00,\xa0\x00\x00\x04\x00\x01\x010\x00\x00\x00Prefngle name="randRotEnd" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="7d755f67-9943-4d08-b439-ce9215f3a028" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.417" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnBulletTick" time="0.200" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetPosActorId" objectName="None" id="-1" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="referenceObjectId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="ActionName" value="prefab_characters/prefab_hero/190_zhugeliang/skill/AutoChess/aca1b1" refvalue="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpecialBuffEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bActionCtrlObjs" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleTeamNotSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="MoveBulletDuration0" eventType="MoveBulletDuration" guid="a4b4420f-87ae-4a8f-8c74-f5b800394aec" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.367" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="MoveBulletDuration" time="0.000" length="0.533" isDpeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50002\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50000\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xe4\x01\x00\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00L\x01\x00\x00\x01\x00\x00\x00D\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdd\x00\x00\x00\x02\x00\x00\x00\x8c\x00\x00\x00\x06\x00\x00\x00v1z\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/Common_Effects/EF_PVP_M_11DefenseTower_Blue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00)\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x8d\x02\x00\x00\x02\x00\x00\x00B\x01\x00\x00t name="\xe5\xa2\x9e\xe5\x8a\xa0\xe9\x87\x91\xe9\x92\xb1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\x8b\xb1\xe9\x9b\x84\xe7\x94\x9f\xe5\x91\xbd\xe6\x97\xb6\xe9\x95\xbf"/>\n\t\t\t\t\t<uint name="\xe7\xa6\xbb\xe5\xbc\x80\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85\xe4\xb8\x80\xe5\xae\x9a\xe8\x8c\x83\xe5\x9b\xb4\xe5\x90\x8e\xe6\xb8\x85\xe9\x99\xa4BUFF"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90"/>\n\t\t\t\t\t<uint name="\xe9\x99\xa4\xe7\x9b\xae\xe6\xa0\x87\xe5\xa4\x96\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe9\x80\x9f\xe6\x8a\xb5\xe6\x8a\x97"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa3\xe9\x99\xa4\xe5\x87\x8f\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\xad\xbb\xe4\xba\xa1"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe6\xb6\x88\xe8\x80\x97\xe5\x89\x8a\xe5\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\xb6\xb3\xe7\x90\x83\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe5\xa5\x89\xe7\x8c\xae"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe8\xa7\x92\xe8\x89\xb2\xe9\x87\x8d\xe7\x94\x9f"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe8\x8e\xb7\xe5\x8f\x96\xe5\x89\x8a\xe5\x87\x8f\xe6\xaf\x94\xe4\xbe\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5\xe9\x98\xb2\xe5\xbe\xa1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe4\xba\x92\xe7\x9b\xb8\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xb8\xbb\xe4\xba\xba\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe5\x8c\x96\xe7\xbb\x99\xe5\xae\xa0\xe7\x89\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x81\x90\xe6\x83\xa7\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe5\x8d\x95\xe6\xac\xa1\xe4\xbc\xa4\xe5\xae\xb3\xe4\xb8\x8a\xe4\xb8\x8b\xe9\x99\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8a\x80\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\xad"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe8\x80\x97\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc\xe6\x8a\xb5\xe6\x8c\xa1\xe4\xbc\xa4\xe5refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTargetBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTotalHitCount" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEdgeCheck" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bExtraBuff" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_1" value="505100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_2" value="505120" refPSetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetAttackDirDuration" time="0.000" length="0.050" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration0" eventType="ForbidAbilityDuration" guid="70d891be-ca4c-4c49-af6f-53ed54d35f4b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.283" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.200" isD name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x80\x92\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe7\x90\x83\xe6\xa7\xbd\xe4\xbd\x8d"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xb9\xe6\x8d\xae\xe6\x8a\xa4\xe7\x94\xb2\xe5\x80\xbc\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xbc\xe6\x8c\xa1\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\xa4\xa7\xe8\xa7\x86\xe9\x87\x8e\xe5\x8d\x8a\xe5\xbe\x84"/>\n\t\t\t\t\t<uint name="\xe5\x8d\x95\xe4\xb8\xaa\xe6\x8a\x80\xe8\x83\xbd\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\xbc\xb9"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe5\xa4\x8d\xe6\xb4\xbb\xe6\x97\xb6\xe9\x97\xb4"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\xa7\x92\xe8\x89\xb2\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\xa7\xbd\xe4\xbd\x8d\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe9\x95\xbf\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe6\x8d\xa2"/>\n\t\t\t\t\t<uint name="\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xae\xad\xe8\xaf\xab\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe9\x94\x90\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\x87\xbb\xe6\x99\xae\xe6\x94\xbb\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe5\x8f\x97\xe5\x88\xb0\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x83\x8c\xe5\x90\x8e\xe6\x94\xbb\xe5\x87\xbb\xe6\x9a\xb4\xe5\x87\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87\xe8\xbd\xac\xe5\x8c\x96\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3 name="excuteMoveCmd" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="immediaRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayMSES\x07\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000ed9c5e8c7fd9b42e102b09260202589\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00`\xea\x00\x00\x04\x00\x00\x00a\xea\x00\x00\x04\x00\x00\x00b\xea\x00\x00\x04\x00\x00\x00c\xea\x00\x00\x04\x00\x00\x00d\xea\x00\x00\x04\x00\x00\x00e\xea\x00\x00\x04\x00\x00\x00f\xea\x00\x00\x04\x00\x00\x00g\xea\x00\x00\x04\x00\x00\x00h\xea\x00\x00\x04\x00\x00\x00i\xea\x00\x00\x04\x00\x00\x00j\xea\x00\x00\x04\x00\x00\x00k\xea\x00\x00\x04\x00\x00\x00l\xea\x00\x00\x04\x00\x00\x00m\xea\x00\x00\x04\x00\x00\x00n\xea\x00\x00\x04\x00\x00\x00o\xea\x00\x00MSES\x07\x00\x00\x00\xb6\x00\x00\x00\x00\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0024e234988d548d1822de209cfbd17add\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00|\x01\x00\x00\xe9\x03\x00\x00\x05\x00\x00\x00Body\x00\x05\x00\x00\x00Hair\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_512.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_512_Mask.bytes\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_256.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_256_Mask.bytes\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00x\x01\x00\x00\xea\x03\x00\x00\x05\x00\x00\x00Body\x00\x01\x00\x00\x00\x00O\x00\x00\x00ChParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSpecifiedDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="specifiedDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReachDestStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bStopOnNavEdge" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDelayLeave" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="randomRotateRange" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepRelateDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOptimizeLanding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontFallInWall" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration1" eventType="HitTriggerDuration" guid="ed80eb7a-cbd8-4b36-a5da-860e3ab6f453" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.383" exeProSmall" type="int" value="5000" />\r\n    <par name="c_HideContinueSelfHP_ConSmall" type="int" value="7000" />\r\n  </pars>\r\n  <node class="SelectorLoop" version="1" id="0">\r\n    <node class="WithPrecondition" version="1" id="40">\r\n      <node class="Action" version="1" id="42">\r\n        <property Method="Self.NucleusDrive::Logic::ActorBaseAgent::IsDeadState()" />\r\n        <property PreconditionFailResult="BT_FAILURE" />\r\n        <property ResultOption="BT_INVALID" />\r\n      </node>\r\n      <node class="Sequence" version="1" id="51">\r\n        <node class="Action" version="1" id="25">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SetCurrCombatDecision(Idle,32)" />\r\n          <property PreconditionFailResult="BT_FAILURE" />\r\n          <property ResultOption="BT_INVALID" />\r\n        </node>\r\n        <node class="Action" version="1" id="41">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SwitchMicroTree(&quot;WrapperAI/Hierarchical/MicroAIs/HeroMicroIdelAI&quot;,true)" />\r\n="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceClearSkillIndicator" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="a74d46ba-4213-46ba-a7ec-e1f30bd87c8a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.917" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.400" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReturnCacheWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill1"!\x00E/\x07\xb9T\x0e\x00\x00T\x0e\x00\x00\x1d\x00\x00\x00156_ZhangLiang/skill/A4B1.xml\xef\xbb\xbf<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n  <TemplateObjectList>\r\n    <TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" />\r\n    <TemplateObject objectName="target" id="1" isTemp="false" />\r\n    <TemplateObject objectName="bullet" id="2" isTemp="true" />\r\n  </TemplateObjectList>\r\n  <RefParamList>\r\n    <uint name="156a4b1" value="0" refParamName="" useRefParam="false" />\r\n  </RefParamList>\r\n  <Action tag="" length="5.000" loop="false">\r\n    <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="a108b9de-b380-464d-ad3f-97838128e929" enabled="true" refParamName="" useRefParam="false" r="0.417" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="3.000" isDuration="true">\r\n        <String name="OutputLiteBulletName" value="156a4b1" refParamName="" useRefParam="false" />\r\n        <uint name="ConfigID" valisDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x80\xe8\x83\xbdCD"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe7.String\x0f\x00\x00\x00\x05\x00\x00\x00VSpell3\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\t\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xa2\x00\x00\x00\x02\x00\x00\x00Q\x00\x00\x00\x06\x00\x00\x00v1?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x11\x00\x00\x00\x05\x00\x00\x00VSpell3_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\x1c\x00\x00\x00\xe0\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0055da304ff85c361e25965639354f5378\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00%w\x00\x00rRepeatedly" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="overrideCDValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="triggerRatio" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xa0\x04\xec\x038=\x00\x008=\x00\x00\x1a\x00\x00\x00107_Zhaoyun/skill/A1E1.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="0.500" loop="false">\n\t\t<Track trackName="FilterTargetType6" eventType="FilterTargetType" guid="20f64bb4-0d0e-40ed-91b4-7ee34475407e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.083" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="FilterTargetType" timetem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/M1A2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00:\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x82\x00\x00\x00\x06\x00\x00\x00v1p\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/PassiveResource/JungleHeal\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00;\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x83\x00\x00\x00\x06\x00\x00\x00v1q\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/PassiveResource/JungleHealB1\x04\x00\x00\x00\x04\x00cts/hero_skill_effects/199_li/li_attack01_spll01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe0\x00\x00\x00\x02\x00\x00\x00\x8f\x00\x00\x00\x06\x00\x00\x00v1}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/Li_attack_spell02_trail\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdb\x00\x00\x00\x02\x00\x00\x00\x8a\x00\x00\x00\x06\x00\x00\x00v1x\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03b\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xda\x00\x00\x00\x02\x00\x00\x00\x89\x00\x00\x00\x06\x00\x00\x00v1w\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03\x04\x00\x00\x00\x04\x00em.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/999_ChessPlayer/99940_ChessPlayer_Show2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00~\x01\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\x1b\x01\x00\x00\x02\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00\xb3\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00W\x00\x00\x00\x01\x00\x00\x00O\x00\x00\x00\t\x00\x00\x00Scale:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.3\x04\x00\x00\x00\x04\x00\x00\x00i\x00\x00\x00!\x00\x00\x00bShadowCameraFollowLobbyActor<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x19\x00\x00\x00runAnimationBaseSpeed;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\r\x00\x00\x00\x05\x00\x00\x00V0.86\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V3000\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0e\x00\x00\x00LobbyScale8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00alue="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID" value="11601" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseCombo" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID1Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkillLevel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="11600" ref\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00(#\x00\x00L\x1d\x00\x00p\x17\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x02\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x10\'\x00\x00c\x00\x00\x00X\x00\x00\x00\x08\x00\x00\x00\x03\x00\r\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\xb9\xb3\xe5\x88\x86\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x88\x13\x00\x00\x01\x03\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x10\'\x00\x00{\x00\x00\x00Y\x00\x00\x00\x08\x00\x00\x00\x04\x00%\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x02\x00\x02\x00\x10\'\x00\x00p\x17\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00p\x17\x00\x00\x00\x10\'\x00\x00x\x00\x00\x00Z\x00\x00\x00\x08\x00\x00\x00\x05\x00"\x00\x00\x00\xe9\x98\xb5\xe8\x90\xa5\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x8a\xa9\xe6\x94\xbb\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00Prefab_Hero/510_Liliana/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xe9a\x8a\x18W5\x00\x00W5\x00\x003\x00\x00\x00Prefab_Hero/510_Liliana/510_Liliana_actorinfo.bytesW5\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x035\x00\x00\x0e\x00\x00\x00Y\x00\x00\x00\r\x00\x00\x00ActorName@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x12\x00\x00\x00\x05\x00\x00\x00V\xe8\x8e\x89\xe8\x8e\x89\xe5\xae\x89\x04\x00\x00\x00\x04\x00\x00\x00\xeb\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa3\x01\x00\x00\x03\x00\x00\x00\x89\x00\x00\x00\x0b\x00\x00\x00Elementr\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/510_Liliana/5101_Liliana_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x89\x00\x00\x00Param="false"/>\n\t\t\t\t<int name="iDelayDisappearTime" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\xad\xbb\xe4\xba\xa1\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb6\xe4\xbb\x96\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe6\x88\x98\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe6\x96\x97\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe9\x9d\x9e\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bExcludeSpecialActor"TPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00J\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe3\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x06\x00\x00\x00v1\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/Prefab_Soldier/New_Truck/skill/monster_atk_bullet_noaoe\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00=\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x85\x00\x00\x00\x06\x00\x00\x00v1s\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringE\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00C\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdc\x00\x00\x00\x02\x00\x00\x00\x8b\x00\x00\x00\x06\x00\x00\x00v1y\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9a\x01\x00\x00\x0c\x00\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/common_effects/allhero_jiaxue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V4\x04\x00\x00\x00\x04\x00\x00\x00>\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x06\x00\x00\x00v1t\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringF\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/526_Summoner/5261_Summoner_LOD1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00<\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x84\x00\x00\x00\x06\x00\x00\x00v1r\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Birth1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe1\x00\x00\x00\x02\x00\x00\x00\x90\x00\x00\x00\x06\x00\x00\x00v1~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Summoner_pet_death\x04\x00\x00ram="false"/>\n\t\t\t\t<bool name="bFilterSameCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlySelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyHostHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRevive" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="attackType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x89\x80\xe6\x9c\x89\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x91\xe6\x88\x98\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x9c\xe7\xa8\x8b\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bSelectJob" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="jobType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="N/A"/>\n\t\t\t\t\t<uint name="\xe5\x9d\xa6\xe5\x85\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe5\xa3\xab"/>\n\t\t\t\t\t<uint name="\xe5\x88\xba\xe5\xae\xa2"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe5\xb8\x88"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x84\xe6\x89\x8b"/>\n\t\t\t\t\t<uint name="\xe8\xbe\x85\xe5\x8a\xa9"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterGrouped" val1_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x17\x00\x00\x00ArtLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa8\x01\x00\x00\x03\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow1\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow2\x04\x00\x00\x00\x04\x00\x00\x00\x88\x00\x00\x00\x0b\x00\x00\x00Elementq\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamerao\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Cam\x04\x00\x00\x00\x04\x00\x00\x00\x0e\x18\x00\x00\x0e\x00\x00\x00SkinPrefabG\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement[]\x04\x00\x00\x00\xb1\x17\x00\x00\x03\x00\x00\x00\xc2\x07\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00j\x07\x00\x00\x06\x00\x00\x00\xe9\x01\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x9d\x01\x00\x00\x03\x00\x00\x00\x87\x00\x00\x00\x0b\x00\x00\x00Elementp\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x000986.wem\x007\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00+\x00\x00\x00Sound/Android/Chinese(Taiwan)/97838123.wem\x008\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/987101814.wem\x008\x00\x00\x00\xe4\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/994406221.wem\x008\x00\x00\x00\xe5\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995073947.wem\x008\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995257090.wem\x00$\x00\x00\x00\xe7\x00\x00\x00\x04\x00\x00\x00\x18\x00\x00\x00AssetBundle/Show/BG/*.*\x00E\x00\x00\x00\xe8\x00\x00\x00\x01\x00\x00\x009\x00\x00\x00AssetBundle/Show/Hero/133_DiRenJie_show_base.assetbundle\x00A\x00\x00\x00\xe9\x00\x00\x00\x03\x00\x00\x005\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_DiRenJie_Show.bnk\x00+\x00\x00\x00\xea\x00\x00\x00\x05\x00\x00\x00\x1f\x00\x00\x00AssetBundle/Modules/Soccer/*.*\x00-\x00\x00\x00\xeb\x00\x00\x00\x05\x00\x00\x00!\x00\x00\x00AssetBundle/Modules/FiveCamp/*.*\x00/\x00\x00\x00\xec\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_Zhaoyun_SFX.bnk\x00>\x00\x00\x00\xed\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_Zhaoyun_VO.bnk\x00/\x00\x00\x00\xee\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_XiangYu_SFX.bnk\x00>\x00\x00\x00\xef\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_XiangYu_VO.bnk\x003\x00\x00\x00\xf0\x00\x00\x00\x03\x00\x00\x00\'\x00\x00\x00Sound/Android/Hero_WangZhaoJun_SFX.bnk\x00B\x00\x00\x00\xf1\x00\x00\x00\x03\x00\x00\x006\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_WangZhaoJun_VO.bnk\x00?\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_LiuShan_SFX.bnk\x00>\x00\x00\x00\xf3\x00\x00\x00\x03\x00\x00\x00useRefParam="false"/>\n\t\t\t\t<String name="endClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayEndClipName" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTriggerTick0" eventType="ChangeSkillTriggerTick" guid="7e6b69c3-4a8c-40e5-bbc7-971898233929" enabled="true" useRefParam="false" refParamName="" r="0.800" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ChangeSkillTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="effectTime" e="\xe4\xb8\x8d\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="interuptAutoAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a66c0c5d-659b-4258-b6f7-6630f5046041" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.117" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="taMSES\x07\x00\x00\x00}\x00\x00\x00f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e0a70c7ddff5db1861c7359c802ff1eb\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00y\x00\x00\x00\x01\x00\x00\x00\x01\x01\x14\x00\x00\x00BB2CD71CABB8E0D8_##\x00=\x00\x00\x00UGUI/Particle/UI_MapCircle_effect/UI_MapCircle_effect_Yellow\x00\x14\x00\x00\x008574E33444BD2708_##\x00\x01\x00y\x00\x00\x00\x02\x00\x00\x00\x01\x01\x14\x00\x00\x00033F49AD5A74\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00K\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe4\x00\x00\x00\x02\x00\x00\x00\x93\x00\x00\x00\x06\x00\x00\x00v1\x81\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringS\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xab\x02\x00\x00\x02\x00\x00\x00Q\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xea\x00\x00\x00\x02\x00\x00\x00\x99\x00\x00\x00\x06\x00\x00\x00v1\x87\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringY\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/chusheng_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x01\x00\x00\x0b\x00\x00\x00uncInstant0" eventType="SkillFuncInstant" guid="8d09eb2f-50ed-4358-a741-27ca7e1a94dd" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.667" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillFuncInstant" time="0.000" isDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration12" eventType="ForbidAbilityDuration" guid="ae7adc4b-a73f-4229-a4f1-dd860c67f460" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.117" b="0tion" x="0" y="0" z="1500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHeroEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseIndicatorDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="targetdir" useRefParam="true"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" vaorceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetCollisionTick" time="0.180" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="type" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="BOX"/>\n\t\t\t\t\t<uint name="SPHERE"/>\n\t\t\t\t\t<uint name="CYLINDERSECTOR"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bIsBlockMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderLine" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockJungleMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="blockCampType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x95\x8c\xe5\xaf\xb9\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe8\x87\xaa\xe5\xb7\xb1\xe9\x98\xb5\xe8\x90\xa5"22C6_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00e2\x00\x00f2\x00\x00g2\x00\x00h2\x00\x00i2\x00\x00j2\x00\x00k2\x00\x00l2\x00\x00m2\x00\x00n2\x00\x00\xe88\x01\x00\x02\x00\x00\x00x\x05\x00\x00\x14\x05\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\x1e\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\xe2\x04\x00\x00x\x05\x00\x00\x14\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\x05\x00\x00\x00\x97\x04\x00\x00\x82\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00E7CA65090D658757_##\x00\x0e\x00\x00\x00GongBenWuZang\x00\x01\x14\x00\x00\x00C2F5E48F7D5C72F0_##\x00\x07\x00\x00\x00301300\x00L\x00\x00\x00Prefab_Characters/Prefab_Hero/130_GongBenWuZang/130_GongBenWuZang_actorinfo\x00\x01\x00\x00\x00\x01X\x1b\x00\x00\xd7\r\x00\x00=\x00\x00\x00\xaaG\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x89\x00\x00\x00P\x00\x00\x00\xd8\x0e\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00\xc0\xc6-\x00(\x17\x02\x00\x00\x00\x00\x00`[\x03\x00X\x0f\x02\x00\xd32\x00\x00\x00\x00\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xd22\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xdc2\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xe62\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00\x06\x00\x00\x00\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x004744E357C306D3C2_##\x00\x01\x11\x00\x00\x00\x19\x00\x00\x00WrapperAI/Hero/HeroLowAI\x00\x1c\x00\x00\x00WrapperAI/Hero/HeroSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmNormalAI\x00"\x00\x00\x00WrapperAI/Hero/HeroFiveCampSimple\x00\x02\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00BB3239B9CC0563BF_##\x00\x02\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00200065368D0DBAAB_##\x00\x19\x00\x00\x00Play_bobao_gongbenwuzang\x00\x01\x00\x00\x002\x00\x00\x00Prefab_Characters/Prefab_Hero/commonresource/Born\x007\x00\x00\x00PrZ\xf9\xd8O\xb7F\x1bLuaS\x01\x19\x93\r\n\x1a\n\x04\x04\x08\x08xV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(w@\x01<@Assets/Prefabs/Lua/AOV/MagicLab/MagicLabRewardItemView.lua\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x14\x00\x00\x00\x03\x00@\x00N@\x00\x00\x83\x80@\x00\x93\xc0@\x01\x04\x80\x80\x01C\x00A\x00\x8e@\x01\x00D\x80\x00\x01\x8c\x00\x00\x00\x07\x80\x00\x83\x8c@\x00\x00\x07\x80\x80\x83\x8c\x80\x00\x00\x07\x80\x00\x84\x8c\xc0\x00\x00\x07\x80\x80\x84\x8c\x00\x01\x00\x07\x80\x00\x85\x0b\x00\x00\x01\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06Class\x04\x17MagicLabRewardItemView\x04\x02N\x04\x0bCUILuaView\x04\x08require\x04\x19AOV.MagicLab.MagicLabSys\x04\x0edocumentation\x04\rOnViewInited\x04\x08Refresh\x04\nSetCDNPic\x04\nItemClick\x01\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x06\x00\x00\x00\r\x00\x00\x00\x01\x00\x02\x17\x00\x00\x00\x0b\x00\x80\x00C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S@\xc1\x00\x07@\x00\x80C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc1\x00\x07@\x00\x83C@@\x00S@\xc2\x00\x07@\x00\x84C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc2\x00\x07@\x00\x85\x0b\x00\x80\x00\x0c\x00\x00\x00\x04\x0cListElement\x04\x03CS\x04\x07Assets\x04\x08Scripts\x04\x03UI\x04\x15CUIListElementScript\x04\x07CDNpic\x04\x10CDNPicComponent\x04\x08BoxText\x04\x06Text2\x04\x0bClickEvent\x04\x0fCUIEventScript\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x01\x00\x00\x00\x05self\x00\x00\x00\x00\x17\x00\x00\x00\x01\x00\x00\x00\x05_ENV\x00\x0f\x00\x00\x00\x17\x00\x00\x00\x01\x00\x05\r\x00\x00\x00\x07@@\x80S\x80@\x00\x8c\x00\x00\x00G\x80\x80\x81S\x00A\x00l@\xc1\x00\xc3\x80A\x00\x03\xc1A\x00\x13\x01B\x02\xc4\x00\x00\x01D\x80\x00\x00G\x80\xc2\x84\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06BoxID\x13\xff\xff\xff\xff\xff\xff\xff\xff\x04\x0bClickEvent\x04\x08onClick\x04\x0cListElement\x04\rGetComponent\x04\x07typeof\x04\x02N\x04\x0fCUIEventScript\x04\x08enabled\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x00\x00\x02\x04\x00\x00\x00\x05\x00\x00\x00,\x00@\x00\x04@\x00\x01\x0b\x00\x80\x00\x01\x00\x00\x00\x04\nItemClick\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05self\r\x00\x00\x00\x10\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x14\x00\x00\x00\x16\x00\x00\x00\x16\x00\x00\x00name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="6c8555eb-3d65-40dc-b96b-22085a7b349f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.MSES\x07\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f36f7a0cf63b751b43487af3ac37a561\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00HB\x00\x00\xc8B\x14\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0A\x00\x00HB\x14\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00 A\x00\x00\xf0A\x14\x00\x00\x00\x14\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0@\x00\x00 A\x14\x00\x00\x002\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\xa0@\x14\x00\x00\x00d\x00\x00\x00\xf4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x14\x00\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x14\x00\x00\x00\xe8\x03\x00\x00\x88\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7\xa3=\x14\x00\x00\x00\x88\x13\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xccL=MSES\x07\x00\x00\x00^\x00\x00\x00\x06\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ea39319bc554c025c5f107f401c732b8\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00e\x00\x00\x00\x14\x00\x00\x00C235D3F892E815B5_##\x00\x14\x00\x00\x006E67E299EE10381A_##\x00\n\x00\x00\x00touxiang1\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00f\x00\x00\x00\x14\x00\x00\x008BD1A0FD4DFCA919_##\x00\x14\x00\x00\x005696820E83B5B08F_##\x00\n\x00\x00\x00touxiang2\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00g\x00\x00\x00\x14\x00\x00\x007B989B6E5EDFA305_##\x00\x14\x00\x00\x00498F4E0296"" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDeadControlHero" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCurrentTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMoveDirection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Angle" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBigMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyMe" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="bulletID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCantAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType1" valu\x00\x00\x00\x04\x00\x00\x00\x91\x00\x00\x00\x0b\x00\x00\x00Elementz\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_LOD3\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_Show1\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00]\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0f\x00\x00\x00SavedSkinId7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00CrossFadeTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.3\x04\x00\x00\x00\x04\x00\x00\x00#\x04\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\xc0\x03\x00\x00\x02\x00\x00\x00\xda\x01\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00~\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00x8\x00\x00\x00\x03 r="0.100" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack5" eventType="StopTrack" guid="b3cfc329-c442-4487-ab73-1d5ffcf3a8d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.133" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="2" guid="d1939f1f-84aa-46f2-9322-abcc2231ad1a" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x120X\xbc\xa5S\x00\x00\xa5S\x00\x00#\x00\x00\x00196_Elsu/skill/AfterLastEvent="true">\n\t\t\t<Event eventName="HitTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="hitTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInheritRefParams" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="triggerId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bulletHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="victimId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="lastHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSkillCombineChoose" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="1841001" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" val\t<Vector3i name="offsetDir" x="0" y="0" z="0" refParamName="_TargetDir" useRefParam="true"/>\n\t\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="distance" value="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="18000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="gravity" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAdjustSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="1e0b1d40-f329-4718-b4d0-d5c0caaaa1e4" enabled="true" lod="0" useRefParam="false" refParamName="" r="1.000" g="0.233" b="me="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.650" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="1.267" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="clipName" value="Atk1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontReplaceSameAnim" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="subLayer" .Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00I\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe2\x00\x00\x00\x02\x00\x00\x00\x91\x00\x00\x00\x06\x00\x00\x00v1\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acA1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00O\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x97\x00\x00\x00\x06\x00\x00\x00v1\x85\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringW\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acmakeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9b\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x10\x01\x00\x00\x01\x00\x00\x00\x08\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa1\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00\x06\x00\x00\x00v1>\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x10\x00\x00\x00\x05\x00\x00\x00V6710002\x04\x00\x00\x00\x04\x004_##\x00>\x00\x00\x00\x1e\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002B5B6A1F7A9007E5_##\x00?\x00\x00\x00$\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00EE2974C205C472E7_##\x00\x01\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002521BBD3EE0BDF80_##\x00<\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x01<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":68}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00BDB77D73EF3CDFB6_##\x00\x03\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00898A75C147D555B3_##\x00\x06\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00FA3AF0603BDD9365_##\x00\x07\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x0051ED5D030B64764D_##\x00\n\x00\x00\x00\t\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00C50583CB6167E4E5_##\x00\x0b\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd8\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x004721F4D35F33FCA5_##\x00\x0c\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x00<\x00\x00\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00HF\xa6,D\x0e\x00\x00D\x0e\x00\x00+\x00\x00\x00177_ChengJiSiHan/skill/AutoChess/acA1E3.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList/>\n\t<Action tag="" length="0.300" loop="false">\n\t\t<Track trackName="SkillFuncDuratio-9322-abcc2231ad1a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.833" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticle" time="0.000" length="1.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet1" id="3" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/174_yuji/yuji_attack01_spell02" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="dontShowIfNoBindPoint" valtem.Int32]\x04\x00\x00\x00\xeb\x00\x00\x00\x02\x00\x00\x00\x9a\x00\x00\x00\x06\x00\x00\x00v1\x88\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringZ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huijidi_dead\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00S\x0e\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xbb\r\x00\x00\x0b\x00\x00\x00\x1f\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb8\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x06\x00\x00\x00v28\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0b\x00\x00\x00\x05\x00\x00\x00V10\x04\x00\x00\x00\x04\x00\x00\x00@\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd9\x00\x00\x00\x02\x00\x00\x00\x88\x00\x00\x00\x06\x00\x00\x00v1v\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/109_daji/daji_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V3\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneSkillSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplaceHPBarImmuneSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCallBoss" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidExtraBtnSlot1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="43618e12-f288-4877-9d44-4cb1ef89f0a2" enabled="true" useRefParam="false" refParamName="" r="0.467" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.333" isDur1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/536_Ninja/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/544_Painter/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xc5z\x03\xef/\x0c\x00\x00/\x0c\x00\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81`\x00\x00\x00Prefab_Hero/544_Painter/544_Painter_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xe1\x00\x00\x00\xe0\x0c\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00Prefab_Hero/148_JiangZiYa/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00h-\x11\x99U\x1f\x00\x00U\x1f\x00\x007\x00\x00\x00Prefab_Hero/148_JiangZiYa/148_JiangZiYa_actorinfo.bytesU\x1f\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x01\x1f\x00\x00\x0f\x00\x00\x00]\x00\x00\x00\r\x00\x00\x00ActorNameD\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x16\x00\x00\x00\x05\x00\x00\x00V148_JiangZiYa\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xaf\x01\x00\x00\x03\x00\x00\x00\x8d\x00\x00\x00\x0b\x00\x00\x00Elementv\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplayWhenChangeMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTrailProtect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepChildScale" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/HeroStun\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x008\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x80\x00\x00\x00\x06\x00\x00\x00v1n\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String@\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x004\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcd\x00\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x06\x00\x00\x00v1j\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xbc\x07\x00\x00\x0e\x00\x00\x00animationsw\x00\t\t<String name="SpecialActionName" value="prefab_characters/prefab_hero/115_gaojianli/skill/a1b2" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDeadRemove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmeExcute" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeEternal" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletTypeId" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletUpperLimit" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpawnBounceBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="bulletSkillType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\xbb\x98\xe8\xae\xa4\xe7\xb1\xbb\xe5\x9e\x8b_0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x81\xe8\xae\xb8\xe7\x89\xb9\xe6\xae\x8a\xe6\x89\x93\xe6\x96\xad_1"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDestroyedBySpecialBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTrigger\t\t\t\t<bool name="forbidFilterSkill4" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill5" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill6" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill7" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill8" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill10" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill11" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSummonerSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterMapSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterEquipActiveSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterActiveSame="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRealTimeSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOpenSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBlockObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkin" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRecordObjPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="recordTargeID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TrackObject name="trackId" id="-1" guid="00000000-0000-0000-0000-000000000000" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetCollisionTick0" eventType="SetCollisionTick" guid="dcd824ef-bb03-4fc8-bf5c-a64a29c3c0\t<int name="ExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Rotation" value="160" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="HeightGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="RotationGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</EMSES\x07\x00\x00\x00\x1c\x00\x00\x00\x0e\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009b0dbb76c4f9d3da6c78991155e5e1c2\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\r\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x91\xb0\x00\x00\x08\x00\x00\x00RargetSkillCombine_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_3" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBullet" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="BulletActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/extend/exs2b1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeImmeExcute" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTriggerObj" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceUseTriggerObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerMode" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBounceBullete"/>\n\t\t\t\t<int name="triggerInterval" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorInterval" value="30" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterFriend" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterMonter" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterChest" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEye" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMyself" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" \xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x85\xe9\x80\x9f\xe5\xa4\x8d\xe6\xb4\xbb"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe7\x90\x83\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\xa9\xb1\xe6\x95\xa3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x85\x8d\xe7\x96\xab\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe8\x8e\xb7\xe5\x8f\x96\xe8\xa7\x86\xe9\x87\x8e\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\xba\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9f\xa7\xe6\x80\xa7\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x86\xb7\xe5\x8d\xb4\xe7\xbc\xa9\xe5\x87\x8f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x97\xe6\x9a\xb4\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5RVO"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe6\x9d\xa1\xe4\xbb\xb6\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9b\xb4\xe6\x8d\xa2\xe8\xa1\x80\xe6\x9d\xa1\xe9\xa3\x8e\xe6\xa0\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x97\xe6\x8e\xa7\xe9\xa2\x9d\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"<int name="level3Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level4Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level5Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level6Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOtherSkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillUseCacheTick0" eventType="SkillUseCacheTick" guid="53c33571-7838-484f-9f06-7b93d4bc28e0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.217" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillUseCacheTick" time="0.350" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="e8a22af8-4078-4313-893b-f729c0f328ed" enabled="false" useRalse"/>\n\t\t\t\t<bool name="bUseRealScaling" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseHeroLocalForward" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRandomRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="randRotBegin" x="0.ramName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="612800" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckCondition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOvertimeCD" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSendEvent" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="attackTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="level0Id" valuname="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x89\x80\xe6\x9c\x89\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bVaildBlockForSelfTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVaildBlockForEnemyTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Pos" x="0" y="0" z="-1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Size" x="2000" y="10000" z="3000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="PosList" refParamName="" useRefParam="false" type="Vector3i"/>\n\t\t\t\t<int name="Radius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorRadius" value="1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Height" value="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Degree" value="160" refP\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/commonresource/Dead_Born\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x003\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcc\x00\x00\x00\x02\x00\x00\x00{\x00\x00\x00\x06\x00\x00\x00v1i\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String;\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x000\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc9\x00\x00\x00\x02\x00\x00\x00x\x00\x00\x00\x06\x00\x00\x00v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/A1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x002\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcb\x00\x00\x00\x02\x00\x00\x00z\x00\x00\x00\x06\x00\x00\x00v1h\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String:\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/\x00h\x00\x00\x00\x01\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V2200\x04\x00\x00\x00\x04\x00\x00\x00g\x00\x00\x00\x0b\x00\x00\x00HudTypeP\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.HudCompType\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00n\x00\x00\x00\x11\x00\x00\x00collisionTypeQ\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum1\x00\x00\x00\x08\x00\x00\x00TypeNucleusDrive.Share.CollisionShapeType\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x01\x00\x00\x14\x00\x00\x00iCollisionCenter&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00x7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V200\x04\x00\x00\x00\x04\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00z7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1600\x04\x00\x00\x00\x04\x00\x00\x00v\x00\x00\x00\x12\x00\x00\x00BtResourcePathX\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String*\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Soldier/BTSoldierNormal\x04\x00\x00\x00\x04\x00\x00\x00\x8d\x00\x00\x00\x0f\x00\x00\x00deadAgePathramName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType2" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBeControledActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyAttackerPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyDeadOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCanntAttackOrgan" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorCount" value="32" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="SelectMode" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x9a\x8f\xe6\x9c\xba\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe8\xa1\x80\xe9\x87\x8f\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x89\xe7\x9c\xbc\xe7\x9a\x84\xe8\xa7\x84\xe5\x88\x99\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="CollideMaxCount" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" am="false" />\r\n        <bool name="bExtraBuff" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOverrideParam" value="false" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam1" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam4" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam5" value="0" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId2" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabl guid="884649fb-eee1-4f09-8e8c-136817834eb9" enabled="true" useRefParam="false" refParamName="" r="0.900" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetBehaviourModeTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delayStopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="deadControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0="SkillInputCacheDuration" time="0.233" length="0.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCacheSkillReCalcLock" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkMoveAbortCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDure"/>\n\t\t\t\t<int name="animatorOverrideLayer" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLoop" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseFadeOutTime" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="fadeOutTime" value="0.200" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="startTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="endTime" value="99999.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeed" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepOldSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="beginClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayBeginCliTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/fireta_hurt_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00825732d46fb1b030cdac35cc22c3f23d\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x07\x00\x00\x00\x14\x00\x00\x00A409CCAC72376898_##\x00\x1c\x00\x00\x00\x1e\x00\x00\x00\x14\x00\x00\x000629BC043F5D2625_##\x00\x1c\x00\x00\x00d\x00\x00\x00\x14\x00\x00\x007D56267D87A29EDD_##\x00\x1c\x00\x00\x00m\x01\x00\x00\x14\x00\x00\x00DFB6F47F471FD135_##\x00\x13\x0f\x00\x00\x08\x00\x00\x00ROOTC\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom.\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSet\x04\x00\x00\x00\xc0\x0e\x00\x00\x01\x00\x00\x00\xb8\x0e\x00\x00\x0e\x00\x00\x00baseSubsetF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSubset\x04\x00\x00\x00\\\x0e\x00\x00\x04\x00\x00\x00l\x05\x00\x00\x0b\x00\x00\x00actionsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xe2\x04\x00\x00\x04\x00\x00\x005\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xce\x00\x00\x00\x02\x00\x00\x00}\x00\x00\x00\x06\x00\x00\x00v1k\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String=\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/Soldier1/skill/M1A1\x04\x00\x00\x00\x04\x00>\n\t\t\t\t<bool name="bTargetPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="targetPosition" x="0" y="0" z="0" refParamName="" useRefParam="true"/>\n\t\t\t\t<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveCollision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="recreateExisting" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="superTranslation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyTranslation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="translation" x="-600" y="1400" z="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableTag" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" va\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c41c436a-6fd5-4207-a69b-f3ffebeadf55" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.583" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDonotAttackToMesh" valuSoundTick7" eventType="PlayHeroSoundTick" guid="a23129b2-cb41-44f8-93ff-cf6c2ceaf519" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="sourceId" objectName="None" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="eventName" value="Play_Meilin_Wanou_Skill_Hit_1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSkinSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="extraSkinId" refParamName="" useRefParam="false" type="uint"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xffZ\x87\xc0\xeaa\x00\x00\xeaa\x00\x00*\x00\x00\x00Prefab_Monster/137_SiMaYi_Pet/skill/A2.xml<?xLLY\x04\x00\x00\x00\x04\x00\x00\x00,\x00\x00\x00\x0b\x00\x00\x00Element\x15\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\x08\x00\x00\x00NULLY\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00A\x06\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe9\x05\x00\x00\x05\x00\x00\x00\x01\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb5\x01\x00\x00\x03\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x07\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb8\x01\x00\x00\x03\x00\x00\x00\x90\x00\x00\x00\x0b\x00\x00\x00Elementy\x00\x00\x00\x03\x00\x00\x00\t\t<bool name="abortFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterDamage" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMoveRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delaySkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="protectAbortLevel" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe4\xbf\x9d\xe6\x8a\xa4"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="ImmuneNegative" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" valu\n        <int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_1" value="523000" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID1Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID2Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID3Probability" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSight" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSkillLevel" value="false" refParamName="" useRefParam="false" />\r\n        <Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\r\n          <uint name="\xe6\x99\xae\xe6\x94\xbb" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd1" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd2" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd3" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd4" />\r\n \x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x0f\x03\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00w\x02\x00\x00\x02\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Bullet\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x006\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcf\x00\x00\x00\x02\x00\x00\x00~\x00\x00\x00\x06\x00\x00\x00v1l\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String>\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Hit\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\xbe\x00\x00\x00:\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00189d89e27401dc8d9af987c9418892f7\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xab\x00\x00\x00\x02\x00\x00\x00\x00\n\x00\x00\x005v5\xe5\x8c\xb9\xe9\x85\x8d\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00Param="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="ReplacementUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x89\xe6\xb0\xb4\xe5\x8a\xa0\xe9\x80\x9f\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="ReplacementSubUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe8\x90\xbd\xe5\x9c\xb0\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bNoDynamicLod" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMeshResouce" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true"/>\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.500" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceForbidding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkillAndHideBtn" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill3" valame="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="refSkillLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="compareOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterMajorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMinorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSoldier" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterOtherMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAddEffectCount" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="f1307d98-07[System.String,System.Int32]\x04\x00\x00\x00\xf2\x00\x00\x00\x02\x00\x00\x00\xa1\x00\x00\x00\x06\x00\x00\x00v1\x8f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Stringa\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_RedTower_High/skill/New_RedTower_High_A1E1_Slow\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75013\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xb4\x04\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00$\x04\x00\x00\x04\x00\x00\x00\x07\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa0\x00\x00\x00\x02\x00\x00\x00O\x00\x00\x00\x06\x00\x00\x00v1=\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0f\x00\x00\x00\x05\x00\x00\x00V750130\x04\x00\x00\x00\x04\x00\x00<TemplateObject name="VirtualAttachBulletId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseAttachBulletShape" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/502_astrid/astrid_natk01_hurt01" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="lifeTime" value="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="bindPointName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="bindRotOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\x9e\x00\x00\x00\x02\x00\x00\x00M\x00\x00\x00\x06\x00\x00\x00v1;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x05\x00\x00\x00VAtk2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00508_Zhadanren/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00508_Zhadanren/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00508_Zhadanren/skill/extend/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x11\xe7\x15!\x06x\x00\x00\x06x\x00\x00#\x00\x00\x00508_Zhadanren/skill/extend/exA4.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t\t<TemplateObject objectName="bullet" id="2" isTemp="true"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="targetdir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Tram="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillCDTriggerTick0" eventType="SkillCDTriggerTick" guid="ed9f0f3d-9931-4fb8-a5fa-b455c6cbe800" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillCDTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSlotType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80'
    ZSTD_LEVEL = 17  
    print('-------------- TẠO COM.GARENA.GAME.KGVN ----------------')
    for inp in listdir('./Pmin_Sources/Resources'):
        break
    def decompress_(strin,ZSTD_DICT=ZSTD_DICT):
        posdecompress = strin.find(b"\x28\xb5\x2f\xfd")
        if posdecompress != -1:
            strin = strin[posdecompress:]
            strin = strin[strin.find(b"\x28\xb5\x2f\xfd"):]
            strin = pyzstd.decompress(strin, pyzstd.ZstdDict(ZSTD_DICT, True))
        return strin
    if os.path.isdir('./com.garena.game.kgvn/') == 0 :
        os.mkdir('./com.garena.game.kgvn/')
        os.mkdir('./com.garena.game.kgvn/files')
        os.mkdir('./com.garena.game.kgvn/files/Resources/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Ages/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Ages/Prefab_Characters/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Ages/Prefab_Characters/Prefab_Hero/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Actor')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Huanhua')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Character')
        with open(f'./pmin_sources/Resources/{inp}/Databin/Client/Character/ResCharacterComponent.bytes','rb') as f:
            a=decompress_(f.read(),ZSTD_DICT)
        with open(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Character/ResCharacterComponent.bytes','wb') as f:f.write(a)
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Motion')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Rank')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Shop')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Skill')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Databin/Client/Sound')
        os.mkdir(f'./com.garena.game.kgvn/files/Resources/{inp}/Prefab_Characters/')
    print('------------------- TẠO XONG RỒI ĐÓ --------------------')
    print('------ ĐANG GIẢI NÉN AGES VÀ PREFAB_CHARACTER ... ------')
    def giai_nen(z,a): 
        import zipfile 
        fantasy_zip = zipfile.ZipFile(z+a)
        fantasy_zip.extractall(z)
        return '\033[1;32mGiai Nen Xong File: ' +a
    t1=f'./Pmin_Sources/Resources/{inp}/Ages/Prefab_Characters/Prefab_Hero/'
    t2=f'./Pmin_Sources/Resources/{inp}/Prefab_Characters/'
    if os.path.isdir(f'./Pmin_Sources/Resources/{inp}/Ages/Prefab_Characters/Prefab_Hero/150_HanXin') == 0 :
        for file in listdir(t2):
            if 'Actor' in file:
                print(giai_nen(t2,file),end='\r')
        for file in listdir(t1):
            if 'Rapid' not in file and 'Newbie' not in file and 'Actor' in file:
                print(giai_nen(t1,file),end='\r')
            if file== 'CommonActions.pkg.bytes':
                print(giai_nen(t1,file),end='\r')
        print(giai_nen(f'./Pmin_Sources/Resources/{inp}/Ages/','Prefab_Gear.pkg.bytes'),end='\r')
    print('--------------- ĐÃ GIẢI NÉN XONG RỒI ĐÓ ----------------')
    print('------------------ BẮT ĐẦU MOD THOI --------------------')
    try:
        folder_mod = sys.argv[1]
    except:
        folder_mod=input('\t\tNhập Folder Để Vào: ')
    n=0;born=8;born_dem = 0;ca='';hasteE1 = 48;hasteE1_leave=41;has = 0
    try:
        with open(f"list_mod.txt", 'r') as f1:
            strin = f1.read()
        HD_e = 's' if 'hd' in strin.lower() else 't'
        list_mod = "\n".join([a for a in strin.split('\n') if 'hd' not in a.lower()])
        with open('list_mod.txt', 'w') as f:
            f.write(list_mod)
    except:
        HD_e='t'
    if HD_e=='' or 's' in HD_e or 'S' in HD_e:
        HD_e=True
    else:
        HD_e=False
        folder_mod=folder_mod
    DeAllSkin='t'
    if DeAllSkin=='' or 's' in DeAllSkin or 'S' in DeAllSkin:
        DeAllSkin=True
    else:
        DeAllSkin=False
    LoiMang='s'
    if LoiMang=='' or 's' in LoiMang or 'S' in LoiMang:
        LoiMang=True
    else:
        LoiMang=False
    def giai_nen(z,a): 
        import zipfile 
        fantasy_zip = zipfile.ZipFile(z+a)
        fantasy_zip.extractall(z)
        return '\033[1;32mGiai Nen Xong'
    def split_code_(data):
        split_code = []
        start_tag = b'    <Track trackName='
        end_tag = b'  </Action>\r\n</Project'

        start_pos = data.find(start_tag)
        while start_pos != -1:
            next_pos = data.find(start_tag, start_pos + len(start_tag))
            if next_pos == -1:
                code = data[start_pos:].replace(end_tag, b'')
            else:
                code = data[start_pos:next_pos].replace(end_tag, b'')
            split_code.append(code)
            start_pos = next_pos

        return split_code
    def tim_guid2(a):
        p=a.find(b'guid="')
        return a[p:a.find(b'"',p+6)]
    def nguon_check(a):
        p=a.split(b'</Track>')
        for i in p:
            if b'CheckSkinIdTick' in i or b'CheckHeroIdTick' in i:
                c=i.find(b'guid="')
                c2=i.find(b'" enabled="')
                code=i[c:c2]
                a=a.replace(code,b'guid="https://www.youtube. com/channel/UCCC_v4jNIW_nn6EmH_6WRDg')
        return a
    def split_code_infos_a(a):
        z=[]
        p=a.find('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">')
        while p!=-1:
            p2=a.find('\n      </Item>',p)
            z.append(a[p+len('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">'):p2])
            p=a.find('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">\n         ',p2)
        return z
    def mod_infos_mac_dinh(a,skinid,List):
        if skinid=='13311':
            a=  a.replace(
                    'Prefab_Characters/Prefab_Hero/133_DiRenJie/1332_DiRenJie_LOD',
                    'Prefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD'
                ).replace(
                    'Prefab_Characters/Prefab_Hero/133_DiRenJie/1332_DiRenJie_Show',
                    'Prefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show'
                ).replace(
                    'Prefab_Characters/Prefab_Hero/133_DiRenJie/1331_DiRenJie_Cam',
                    'Prefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam'
                )
        if skinid=='16707':
            a=  a.replace(
                    'Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_LOD',
                    'Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD'
                ).replace(
                    'Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_Show',
                    'Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show'
                ).replace(
            'Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_Cam</ArtSkinLobbyShowCamera>',
            'Prefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Cam</ArtSkinLobbyShowCamera>\n'
            '         <ArtSkinLobbyShowMovie Var="String" Type="System.String">'
            'Prefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Movie</ArtSkinLobbyShowMovie>'
        )
        if skinid=='11620':
            a= a.replace(
                    'Prefab_Characters/Prefab_Hero/116_JingKe/11621_JingKe_AW1_Show',
                    'Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_04_Show'
                )
            a=a.replace('AW1','AW5')
        #a=a.replace('         </ArtSkinLobbyShowLOD>','         </ArtSkinLobbyShowLOD>\n         <MSAA Var="Enum" Type="Assets.Scripts.GameLogic.EAntiAliasing">2</MSAA>')
        skinid=skinid[:3]+str(int(skinid[3:])+1)
        for skin in split_code_infos_a(a):
            if 'Assets.Scripts.GameLogic.EAntiAliasing' not in skin:
                a=a.replace(skin,skin.replace('         </ArtSkinLobbyShowLOD>','         </ArtSkinLobbyShowLOD>\n         <MSAA Var="Enum" Type="Assets.Scripts.GameLogic.EAntiAliasing">2</MSAA>'))
        for skin in split_code_infos_a(a):
            p=skin.find('_Show')
            if f'/{skinid}_' in skin[:p]:
                break
        skin=skin.replace('<ArtSkinPrefabLOD ', '<ArtPrefabLOD ').replace(
        '</ArtSkinPrefabLOD>', '</ArtPrefabLOD>').replace(
        '<ArtSkinLobbyShowLOD ', '<ArtLobbyShowLOD ').replace(
        '</ArtSkinLobbyShowLOD>', '</ArtLobbyShowLOD>'
        )
        skin=skin[skin.find('<ArtPrefabLOD '):]
        skin=skin.replace('>\n      ','>\n')
        p2=a.find('\n   <SkinPrefab ')
        if skinid in ['5486']:
            p=a.find('</ActorName>\n   ')
            de=a[p+len('</ActorName>\n   '):p2]
        else:
            p=a.find('<ArtPrefabLOD ')
            de=a[p:p2]
        a=a.replace(de,skin,1)
        a=rut_gon_infos(a)
        pz=a.split('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">')
        for skin in split_code_infos_a(a):
            p=skin.find('_Show')
            if f'/{skinid}_' in skin[:p]:
                break
        for i in split_code_infos_a(a):
            a=a.replace(i,skin,1)
        return a
    def xoa_thua_thai(strin):
        return strin
        strin2=strin
        try:
            if b'trackName' in strin2:
                guids = re.findall(rb'guid="(.*?)"', strin)
                for guid in guids:
                    strin=re.sub(rb'guid="\s*'+guid+rb'"',b'guid="TOIBINGU NEN DI REUP CUA DANG PMIN MOD"', strin, flags=re.IGNORECASE)
                trackname = re.findall(rb'Track\s*trackName="(.*?)"', strin)
                for trackname in trackname:
                    strin=re.sub(rb'<Track\s*trackName="\s*'+trackname+rb'"',b'<Track trackName="youtube.com/@hongcogidauma"', strin, flags=re.IGNORECASE)
                strin=re.sub(rb'>\s+<', b'><',strin)
                return strin #.replace(b' refParamName=""',b'').replace(b' isTemp="false"',b'').replace(b'execOnForceStopped="false" execOnActionCompleted="false" ',b'').replace(b' useRefParam="false"',b'').replace(b' value=""',b'')
            else:
                return strin2
        except:
            return strin2
    def skillmark(a,skinid):
        t=b'prefab_skill_effects/hero_skill_effects/'
        d=383
        b=a[d:]
        check=True
        while True:
            c=b[:hex_to_dec(b[:2])+4]
            d=d+len(c)
            if t+skinid[:3] in c:
                p=c.find(t)
                i=0
                while p!=-1:
                    i+=1
                    p2=c.find(b'/',p+len(t))
                    h=c[p-4:p2+1]
                    p=c.find(t,p2)
                break
            if d==len(a):
                check=False
                break
            b=a[d:]
        if check:
            za=c.replace(h,dec_to_hex(hex_to_dec(h[:1])+6)+h[1:]+skinid+b'/')
            za=dec_to_hex(hex_to_dec(za[:2])+6*i)+za[2:]
            a=a.replace(a[:a.find(c)]+c,a[:a.find(c)]+za)
        return a
    def fix_ef(a,ID):
        p=a.find(b'/'+ID+b'/'+ID+b'/')
        while p!=-1:
            a=a.replace(b'/'+ID+b'/'+ID+b'/',b'/'+ID+b'/')
            p=a.find(b'/'+ID+b'/'+ID+b'/')
        return a
    def fix_sound(a,ID):
        p=a.find(b'_skin'+ID+b'_skin'+ID+b'"')
        while p!=-1:
            a=a.replace(b'_skin'+ID+b'_skin'+ID+b'"',b'_skin'+ID+b'"')
            p=a.find(b'_skin'+ID+b'_skin'+ID+b'"')
        return a
    def compress_(input_blob,ZSTD_DICT=ZSTD_DICT):
        output_blob=input_blob
        #return output_blob
        if b'\x22\x4a\x67\x00' not in input_blob and b"\x28\xb5\x2f\xfd" not in input_blob:
                output_blob = bytearray(pyzstd.compress(input_blob, ZSTD_LEVEL, pyzstd.ZstdDict(ZSTD_DICT, True)))
                output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
                output_blob[0:0] = b"\x22\x4a\x00\xef"
                output_blob+=b''
        return output_blob
    def decompress_(strin,ZSTD_DICT=ZSTD_DICT):
        posdecompress = strin.find(b"\x28\xb5\x2f\xfd")
        if posdecompress != -1:
            strin = strin[posdecompress:]
            strin = strin[strin.find(b"\x28\xb5\x2f\xfd"):]
            strin = pyzstd.decompress(strin, pyzstd.ZstdDict(ZSTD_DICT, True))
        return strin
    def code_assetref(code,skinid):
        code=code.lower().replace(b'/'+skinid+b'/',b'/')
        skinid=skinid.decode()[:3]
        with open(f'./Pmin_Sources/Resources/1.58.1/AssetRefs/Hero/{skinid}_AssetRef.bytes','rb') as f:
            a=decompress_(f.read(),ZSTD_DICT)
            a=a.lower()
            if code in a:
                return True
            else:
                return False
    def mod_ef_sound2(a,nh,ID):
        z=[]
        nh=bytes(nh,'utf-8')
        str1 = b"hero_skill_effects/" + nh.lower() + b"/"
        str2 = b"hero_skill_effects/" + nh + b"/"
        str3 = b"Hero_Skill_Effects/" + nh.lower() + b"/"
        str4 = b"Hero_Skill_Effects/" + nh + b"/"
        z.append(str1);z.append(str2);z.append(str3);z.append(str4)
        strsp = b"component_effects/"
        if ID in [b'13311',b'16707',b'11620']:
            for b in z:
                if b in a:
                    a=a.replace(b,strsp+ID+b'/'+ID+b'_5/')
        else:
            for b in z:
                if b in a:
                    a=a.replace(b,b+ID+b'/')
        if ID[:3] == b'190':
            a=a.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/',b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/'+ID+b'/')
        if ID==b'15412':
            a=a.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/15413_HuaMuLan_Red',b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15413_HuaMuLan_Red')
        a=a.replace(b'        <bool name="bAllowEmptyEffect" value="true" refParamName="" useRefParam="false" />\r\n',b'        <bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false" />\r\n')
        return a
    def fix_ef_infos(a,nh,ID):
        z=[]
        
        str1 = "hero_skill_effects/" + nh.lower() + "/"
        str2 = "hero_skill_effects/" + nh + "/"
        str3 = "Hero_Skill_Effects/" + nh.lower() + "/"
        str4 = "Hero_Skill_Effects/" + nh + "/"
        z.append(str1);z.append(str2);z.append(str3);z.append(str4)
        for b in z:
            if b in a:
                a=a.replace(b,b+ID+'/')
        if ID[:3] == b'190':
            a=a.replace('Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/','Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/'+ID+'/')
        def fix_ef(a,ID):
            p=a.find('/'+ID+'/'+ID+'/')
            while p!=-1:
                a=a.replace('/'+ID+'/'+ID+'/','/'+ID+'/')
                p=a.find('/'+ID+'/'+ID+'/')
            return a
        return fix_ef(a,ID)
    def mod_ef_sound(a,nh,ID,file,folder_mod):
        z=[]
        nh=bytes(nh,'utf-8')
        str1 = b"hero_skill_effects/" + nh.lower() + b"/"
        str2 = b"hero_skill_effects/" + nh + b"/"
        str3 = b"Hero_Skill_Effects/" + nh.lower() + b"/"
        str4 = b"Hero_Skill_Effects/" + nh + b"/"
        z.append(str1);z.append(str2);z.append(str3);z.append(str4)
        strsp = b"component_effects/"
        if ID in [b'13311',b'16707',b'11620']:
            for b in z:
                if b in a:
                    a=a.replace(b,strsp+ID+b'/'+ID+b'_5/')
        else:
            for b in z:
                if b in a:
                    a=a.replace(b,b+ID+b'/')
        T=b''
        if (ID == b'51504' and file in ['A1.xml', 'A2.xml', 'A3.xml', 'A4.xml', 'A5.xml', 'S1.xml', 'S11.xml', 'S12.xml', 'S21B0.xml', 'S21B5.xml', 'S2B0.xml', 'S2B1.xml', 'S2B5.xml', 'U1B0.xml']) or (ID == b'11107' and 'E' not in file and 'eath' not in file)  or (ID == b'12304' and 'E' not in file) or (ID == b'15704' and file in ['S1.xml','A1.xml','A3.xml','A4.xml','S2.xml','U1.xml']):
            a=a.replace(b'<String name="clipName" value="',b'<String name="clipName" value="'+ID+b'/')
            def split_code_clipname(data):
                split_code = []
                start_tag = b'    <Track trackName='
                end_tag = b'  </Action>\r\n</Project'

                start_pos = data.find(start_tag)
                while start_pos != -1:
                    next_pos = data.find(start_tag, start_pos + len(start_tag))
                    if next_pos == -1:
                        code = data[start_pos:].replace(end_tag, b'')
                    else:
                        code = data[start_pos:next_pos].replace(end_tag, b'')
                    if b'<String name="clipName" value="' in code:
                        split_code.append(code)
                    start_pos = next_pos

                return split_code
            for code in split_code_clipname(a):
                condition_start = code.find(b'<Condition id="')
                if condition_start != -1:
                    event_start = code.find(b'<Event eventName="')
                    if event_start != -1 and event_start > condition_start:
                        code = code.replace(code[condition_start:event_start], b'', 1)
                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Dance.xml','rb') as f:
                    dance = f.read()
                    dance = dance.replace(b'  </Action>',code+b'  </Action>')
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Dance.xml','wb') as f1:
                        f1.write(dance)
        a=a.replace(b'        <bool name="bAllowEmptyEffect" value="true" refParamName="" useRefParam="false" />\r\n',b'        <bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false" />\r\n')
        #a=a.replace(b'<String name="resourceName"',b'<int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="resourceName"')
        #a=a.replace(b'<String name="clipName"',b'<int name="frameRate" value="120" refParamName="" useRefParam="false" />\r\n        <String name="clipName"')
        de_ef = b'<bool name="bTrailProtect" value="true" useRefParam="false" />\r\n        <bool name="bUseTargetSkinEffect" value="true" useRefParam="false" />\r\n        <String name="resourceName"'
        if 'e' not in file.lower():
            a=a.replace(b'<String name="resourceName"',de_ef)
        if ID[:3] == b'190':
            a=a.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/',b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/'+ID+b'/')
        return a
    def mod_ef_sound_phu_kien(a,nh,ID):
        z=[]
        nh=bytes(nh,'utf-8')
        str1 = b"hero_skill_effects/" + nh.lower() + b"/"
        str2 = b"hero_skill_effects/" + nh + b"/"
        str3 = b"Hero_Skill_Effects/" + nh.lower() + b"/"
        str4 = b"Hero_Skill_Effects/" + nh + b"/"
        z.append(str1);z.append(str2);z.append(str3);z.append(str4)
        strsp = b"component_effects/"
        if ID in [b'13311',b'16707',b'11620']:
            for b in z:
                if b in a:
                    a=a.replace(b,strsp+ID+b'/'+ID+b'_5/')
        else:
            for b in z:
                if b in a:
                    a=a.replace(b,b+ID+b'/')
        if ID[:3] == b'190':
            a=a.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/',b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/'+ID+b'/')
        return a
    def fix_ef_pro_vip(a,z):
        def split_code_fix_ef(data):
            split_code = []
            start_tag = b'    <Track trackName='
            end_tag = b'  </Action>\r\n</Project'

            start_pos = data.find(start_tag)
            while start_pos != -1:
                next_pos = data.find(start_tag, start_pos + len(start_tag))
                if next_pos == -1:
                    code = data[start_pos:].replace(end_tag, b'')
                else:
                    code = data[start_pos:next_pos].replace(end_tag, b'')
                if b'CheckSkinIdTick' in code:
                    split_code.append(code)
                start_pos = next_pos

            return split_code
        for code in split_code_fix_ef(a):
            if True:
                code2=code
                t=b'        <int name="skinId" value="'+z+b'" refParamName="" useRefParam="false" />\r\n'
                e_true=b'        <bool name="bEqual" value="true" refParamName="" useRefParam="false" />\r\n'
                e_false=b'        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n'
                s_true=b'        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />\r\n'
                s_false=b'        <bool name="bSkipLogicCheck" value="false" refParamName="" useRefParam="false" />\r\n'
                t_98=b'        <int name="skinId" value="'+z[:3]+b'98" refParamName="" useRefParam="false" />\r\n'
                t_97=b'        <int name="skinId" value="'+z[:3]+b'97" refParamName="" useRefParam="false" />\r\n'
                ev=b'      </Event>'
                code=code.replace(t+e_true,t_97+e_false).replace(t+s_true,
                t_97+e_false+s_true).replace(t+s_false,
                t_97+e_false+s_false).replace(t+ev,
                t_97+e_false+ev)
                code=code.replace(t+e_false,t_98+e_true)
                a=a.replace(code2,code)
        return a
    def hex_to_dec(a):
        len(a)
        a=a[::-1]
        a=a.hex()
        a=int(a,16)
        return a
    def dec_to_hex(a):
        a=hex(a)[2:]
        if len(a)%2==1:
            a='0'+a
        return (bytes.fromhex(a))[::-1]
    def fix_condition(a):
        p=a.find(b'<Condition id="')
        while p!=-1:
            p2=a.find(b'" guid="',p)
            condition=a[p:a.find(b'" status="',p)]
            ID=a[p2:a.find(b'" status="',p2)]
            check=a[p+15:a.find(b'"',p+15)]
            if len(ID)>10:
                pz=a.split(b'</Track>')
                for i in range(len(pz)):
                    if ID+b'" enabled' in pz[i]:
                        a=a.replace(condition,b'<Condition id="'+str(i).encode('utf-8')+ID)
                        break
            p=a.find(b'<Condition id="',p2)
        return a
    def back_need(a):
        b=0;za=b''
        p=a.find(b'    <Track trackName=')
        while p!=-1 and b!=5:
            p2=a.find(b'    </Track>',p)
            z=a[p:p2+14]
            if b'clipName' in z:
                za+=z
                b+=1
            p=a.find(b'    <Track trackName=',p2)
        return za
    def getint():
        return int.from_bytes(byt.read(4), 'little')

    def  getstr(pos=None):
        if pos is not None:
            byt.seek(pos, 0)
        ofs=getint()
        stri=byt.read(ofs-4)
        return stri.decode()

    def analynode(fid=None, sta=None):
        global i
        if sta==None:
            sta = byt.tell()
        else:
            byt.seek(sta, 0)
        ofs=getint()
        stri=getstr()
        if stri=='Element':
            stri1='Item'
        else:
            stri1=stri
        myid=i
        i=i+1
        byt.seek(4,1)
        aidx=getint()
        ite=False
        attr={}
        for j in range(0,aidx):
            attr1=analyattr()
            if type(attr1)==str:
                text1=attr1
                ite=True
            else:
                attr.update(attr1)
        if fid == None:
            nod[myid] = ET.SubElement(root, stri1, attrib=attr)
        else:
            nod[myid] = ET.SubElement(nod[fid], stri1, attrib=attr)
        if ite==True:
            if text1=='':
                nod[myid].text=' '
            else:
                nod[myid].text=text1
        checkfour()
        chk=sta+ofs-byt.tell()
        if chk>12:
            byt.seek(4,1)
            sidx=getint()
            for h in range (0,sidx):
                attr=analynode(myid,byt.tell())
        byt.seek(sta+ofs,0)

    def analyattr(pos=None):
        if pos==None:
            pos = byt.tell()
        else:
            byt.seek(pos, 0)
        ofs = getint()
        type = getint()
        if type == 5:
            stri = byt.read(ofs - 8).decode()[1:]
            checkfour()
            byt.seek(pos + ofs, 0)
            return stri
        else:
            if type == 6:
                stri = byt.read(ofs - 8).decode()
                if stri[0:2] == 'JT':
                    if stri == 'JTArr':
                        stri = 'Array'
                    elif stri == 'JTPri':
                        stri = 'String'
                    else:
                        stri = stri[2:]
                    name = 'Var'
                else:
                    name = 'Var_Raw'
            elif type == 8:
                stri2 = byt.read(ofs - 8).decode()
                if stri2[0:4]=='Type':
                    stri=stri2[4:]
                    name = 'Type'
                else:
                    stri=stri2
                    name='Type_Raw'
            else:
                stri = byt.read(ofs - 8).decode()
                name = str(type)
                byt.seek(pos + ofs, 0)
            return {name:stri}
    def rut_gon_infos(a):
        pz=a.split('<Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">')
        for i in range(1,len(pz)-1):
            skin=skinA2=pz[i]
            p=skinA2.find('         <PreloadAnimatorEffects')
            while p!=-1:
                p2=p
                p=skinA2.find('         <PreloadAnimatorEffects',p+50)
            if '<PreloadAnimatorEffects Var="Array" Type="System.String[]"/>\n         <LookAt ' in skinA2:skinA2=skinA2[:p2]+'      </Item>\n      '
            else:p2=skinA2.find('         <LookAt Var="Com');skinA2=skinA2[:p2]+'      </Item>\n      '
            a=a.replace(skin,skinA2)
        return a
    def checkfour():
        if getint()!=4:
            byt.seek(-4,1)
    import xml.etree.ElementTree as ET
    def byteint(num):
        return num.to_bytes(4, byteorder = 'little')

    def bytestr(stri):
        outbyte=byteint(len(stri)+4)
        outbyte=outbyte+stri.encode()
        return outbyte

    def byteattr(key,attr):
        if key == 'Var':
            if attr[key] == 'Array':
                stri = 'JTArr'
            elif attr[key] == 'String':
                stri = 'JTPri'
            else:
                stri = 'JT' + attr[key]
            aid = 6
        elif key == 'Var_Raw':
            stri = attr[key]
            aid = 6
        elif key == 'Type':
            stri = 'Type' + attr[key]
            aid = 8
        elif key=='Type_Raw':
            stri=attr[key]
            aid=8
        else:
            import unicodedata
            if unicodedata.numeric(key):
                stri = attr[key]
                aid = int(key)
        stripro=stri.encode()
        outbyte = byteint(len(stripro) + 8) + byteint(aid) + stripro
        return outbyte

    def bytenode(node):
        iftex=False
        if node.tag=='Item':
            name1='Element'
        else:
            name1=node.tag
        name=bytestr(name1)
        attr1=b''
        aindex=len(node.attrib)
        plus=8
        for key in node.attrib:
            attr1=attr1+byteattr(key,node.attrib)
        if (node.text!=None) and (node.text[0:1]!='\n'):
            if node.text==' ':
                stri1=''
            else:
                stri1=node.text
            iftex=True
            stripro=('V'+stri1).encode()
            attr1=attr1+byteint(len(stripro)+8)+byteint(5)+stripro+byteint(4)
            aindex+=1
            plus=4
        attr1=byteint(len(attr1)+plus)+byteint(aindex)+attr1+byteint(4)
        alchild=b''
        if len(node):
            cindex=0
            for child in node:
                alchild=alchild+bytenode(child)
                cindex+=1
            alchild = byteint(len(alchild) + 8) + byteint(cindex) + alchild
        else:
            if iftex==False:
                alchild=byteint(4)
        bnode = name + attr1 + alchild
        bnode = byteint(len(bnode)+4) + bnode
        return bnode
    def ngaunhien():
        nguon_moi=[b'N',b'A',b'M',b'Y',b'E',b'U',b'N',b'H',b'U']
        import random
        a=random.randint(0,len(nguon_moi)-1)
        return nguon_moi[a]

    def ten_skin_mac_dinh(a,ID):
        if True:
            hero=ID[:3]
            p=a.find(dec_to_hex(int(ID.decode()))+b'\x00\x00'+dec_to_hex(int(hero.decode())))
            skin=a[p-4:p+hex_to_dec(a[p-4:p-2])]
            p=a.find(dec_to_hex(int(hero.decode()+'00'))+b'\x00\x00'+dec_to_hex(int(hero.decode())))
            md=a[p-4:p+hex_to_dec(a[p-4:p-2])]
            i1=md[16:34]
            i2=md[44:62]
            i3=skin[16:34]
            i4=skin[44:62]
            skin2=md[:md.find(b'Share')]+skin[skin.find(b'Share'):]
            md2=skin2=dec_to_hex(len(skin2)-4)+skin2[2:]
            md2=md2[:4]+dec_to_hex(int(ID.decode()))+md2[6:]
            skin2=skin2[:36]+dec_to_hex(int(ID[3:].decode()))+skin2[37:]
            a=a.replace(md,md2.replace(i1,i3).replace(i2,i4)).replace(skin,skin2.replace(i1,i3).replace(i2,i4))
        return a
    print(Fore.GREEN+Style.BRIGHT+'Auto Mod Cre By YTB: Pmin Mod'+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+'Facebook: Đoàn Nguyễn Hà Nam'+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+'Zalo: 0357514770'+Style.RESET_ALL)
    print(Fore.YELLOW+Style.BRIGHT+'\tBắt Đầu Mod:\n'+Style.RESET_ALL)
    co_ma_nguon_khong='n'
    i=0;j=1;kz=0;zz=1
    def zipdir(path, ziph):
        for root, dirs, files in os.walk(DIR):
            for file in listdir(DIR2):
                ziph.write(os.path.join(root, file),
                        os.path.relpath(os.path.join(nonee,file),
                                        os.path.join(path, '..')))
    #####

    def ten_skin_hieu_ung(skinid):
        with open('./Pmin_Sources/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            p=a.find(dec_to_hex(skinid)+b'\x00\x00'+dec_to_hex(int(str(skinid)[:3])))
            bien_ve_ef=False
            ten=b''
            skin=b''
            if p!=-1:
                ten=a[p+12:p+31]
                skin=a[p+40:p+59]
                code=a[p-4:p+hex_to_dec(a[p-4:p-2])]
                if b"Skin_Icon_Skill" in code or b"Skin_Icon_BackToTown" in code or skinid==b'53702' or skinid==13204 or skinid==53702 or skinid == 15305:
                    h=b'\x8f'
                else:
                    h=b'PminMod'
                    with open(f'./Pmin_Sources/Resources/1.58.1/Databin/Client/Sound/BattleBank.bytes','rb') as f:
                        a=f.read()
                        a=decompress_(a,ZSTD_DICT)
                        if bytes(str(skinid),'utf-8') in a:
                            h=b'\x8f'
                if b"Skin_Icon_BackToTown" in code or b"Skin_Icon_Animation" in code:
                    bien_ve_ef=True
                if skinid==13204 or skinid==53702 or skinid == 15305:h=b'\x8f'
        a1=''
        a2=''
        if ten!=b'' and skin!=b'':
            for file in os.listdir('./Pmin_Sources/Resources/1.58.1/Languages/VN_Garena_VN'):

                txt=open(f'./Pmin_Sources/Resources/1.58.1/Languages/VN_Garena_VN/{file}','rb')
                a=txt.read()
                a=decompress_(a,ZSTD_DICT)
                p=a.find(ten)
                if p!=-1:
                    a1=a[p+len(ten)+3:a.find(b'\r',p)].decode()
                p=a.find(skin)
                if p!=-1:
                    a2=a[p+len(skin)+3:a.find(b'\r',p)].decode()
            if skinid==b'50118':
                h=b'\x8f'
            return h,a1+' '+a2,bien_ve_ef
        else:
            return b'PMINMOD','',False
    ######
    def find_skin_A(skinid):
        import re
        z=[]
        count_break=0
        for i in range(1,20):
            c=str(i)
            s=skinid[:3]+b'0'*(len(c)%2)+bytes(c,'utf-8')
            s1=s[:3]+bytes(str(i+1),'utf-8')
            d,e,bien_ve=ten_skin_hieu_ung(int(s.decode()))
            check=re.sub(r"\s+", "", e)
            if '[ex]' in e:
                print('\033[1;32m\nSkin [ex]: Có')
                z.append(s1)
                break
            if count_break==3:
                break
            if len(check)<=2:
                count_break+=1
        if z==[]:
            print('\033[1;32m\nSkin [ex]: Không Có')
        return z
    ######
    def tao(folder_mod):
        if True:
            if os.path.isdir('./File_Mod/') == 0 :
                os.mkdir('./File_Mod/')
            if os.path.isdir('./File_Mod/{}/'.format(folder_mod)) == 1 :
                shutil.rmtree('./File_Mod/{}/'.format(folder_mod))
            if os.path.isdir('./File_Mod/{}/'.format(folder_mod)) == 0 :
                os.mkdir('./File_Mod/{}/'.format(folder_mod))
            shutil.copytree('com.garena.game.kgvn','File_Mod/{}/com.garena.game.kgvn'.format(folder_mod))
            for fo in ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire','SeasonPlay']:
                inp=f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/'
                inp2=f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/'
                if os.path.isdir(f'{inp2}{fo}/') == 0 :
                    os.mkdir(f'{inp2}{fo}/')
                for file in listdir(inp+fo):
                    with open(inp+fo+'/'+file,'rb') as f:
                        a=f.read()
                        if file in ['BlueBuff.xml','RedBuff_Slow.xml','Born.xml','Back.xml','Dance.xml','HasteE1.xml','HasteE1_leave.xml']:
                            a=decompress_(a,ZSTD_DICT)
                            if 'Back' in file:
                                back_need_=back_need(a)
                        with open(inp2+fo+'/'+file,'wb') as f:f.write(a)
            os.mkdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero'.format(folder_mod))
        databin = ['Sound','Actor','Skill','Shop','Motion','Huanhua']
        name = ['BattleBank.bytes','ChatSound.bytes','HeroSound.bytes','LobbyBank.bytes','LobbySound.bytes','heroSkin.bytes','HeroSkinShop.bytes','liteBulletCfg.bytes','skillmark.bytes','ResSkinMotionBaseCfg.bytes','ResKillBillboardCfg.bytes','ResPersonalButtonCfg.bytes','organSkin.bytes']
        for data in databin:
            for file in name:
                    try:    
                        with open(f'./Pmin_Sources/Resources/1.58.1/Databin/Client/{data}/{file}','rb') as f:
                            strin = f.read()
                            strin=decompress_(strin,ZSTD_DICT)
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/{data}/{file}','wb') as f1:
                                f1.write(strin)
                    except:
                            pass
        return back_need_
    ten_de_vao_ten=''
    ten_de_vao_ten_dem=1
    back_need_=tao(folder_mod)
    back_folder = ['commonresource','KeySpell','PassiveResource','mowen','Ultrafire','SeasonPlay']
    yena_15412_back=False
    raz_15710_back=False
    murad_13116=False
    cam_xa_goc=100
    ten_de_vao_skill_an=''
    stoptrack_code=b''
    List_skinor_back=[]
    nut_bam_auto_mod=''
    def checkmayyeu():
        mayyeu = open('./list_mod.txt','r')
        return 'mayyeu' not in (mayyeu.read()).lower()
    may_yeu_mod=checkmayyeu()
    txt = open('./list_mod.txt','r')
    for skinid in txt:
        if "%" in skinid:
            cam_xa_goc=int(skinid.replace('%',''))
            cam_xa_goc=str(cam_xa_goc)
        elif 'nut' in skinid.lower():
            nut_bam_auto_mod=skinid.lower()
        elif 'mayyeu' in skinid.lower() or 'rov' in skinid.lower():pass
        else:
            phu_kien=False
            veres_rt=False
            skinid = bytes(skinid,'utf-8')
            skinid=skinid.replace(b'\n',b'').replace(b' ',b'')
            if skinid==b'15412':yena_15412_back=True
            if skinid==b'15710':raz_15710_back=True
            if skinid==b'13116':murad_13116=True
            if skinid==b'5200401' or skinid==b'5200402':
                skinid_veres=skinid
                veres_rt=True
                skinid=b'52007'
            if b'rt' in skinid or b'RT' in skinid:
                
                phu_kien=True
                skinid_phu_kien=skinid
                skinid=skinid[:5]
            for hero_name in listdir('./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/'):
                if '.rar' not in hero_name and '_' in hero_name:
                    hero_name = bytes(hero_name,'utf-8')
                    if skinid[:3]== hero_name[:3]:
                        decompress = hero_name.decode()
                        break
            hieu_ung,tat,check_bien_ve_ef=ten_skin_hieu_ung(int(skinid.decode()))
            print('\033[1;031mSkin:',tat)
            list_skill_an=[]
            check_skill_an=False
            ten_de_vao_ten=ten_de_vao_ten+str(ten_de_vao_ten_dem)+'. '+tat+'\n'
            ten_de_vao_ten_dem+=1
            if True:
                if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero'.format(folder_mod)) == 0 :
                    os.mkdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero'.format(folder_mod))
                if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress)) == 0 :
                    os.mkdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress))
                for filezz in listdir(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/'):
                    if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,filezz)) == 0 :
                        os.mkdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,filezz))
                if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress)) == 0 :
                    os.mkdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress))
                
                #-----------------------------------------------Mod Sound------------------------------------------------------------#

                try:
                    id_mod=dec_to_hex(int(skinid.decode()))
                    id_0=dec_to_hex(int(skinid.decode()[:3]+'00'))
                    print('Mod Sound')
                    if True:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/BattleBank.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x01\x00\x00\x00\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            KatakanaXinhGai=False
                            if pos!=-1:
                                KatakanaXinhGai=True
                                strin = strin.replace(b'\x01\x00\x00\x00\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x01\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                strin = strin.replace(b'\x01\x00\x00\x00\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x01\x00\x00\x00\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/BattleBank.bytes','wb') as f1:
                                    f1.write(strin)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/ChatSound.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1:
                                strin = strin.replace(b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                strin = strin.replace(b'\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/ChatSound.bytes','wb') as f:
                                    f.write(strin)
                        find_back=0
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/HeroSound.bytes','rb') as f:
                            strin = f.read()
                            find_back=strin.count(b'\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            pos = strin.find(b'\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1:
                                strin = strin.replace(b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                strin = strin.replace(b'\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/HeroSound.bytes','wb') as f:
                                    f.write(strin)  
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbyBank.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00\x00\x00\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1:
                                strin = strin.replace(b'\x00\x00\x00\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                strin = strin.replace(b'\x00\x00\x00\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\x00\x00\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbyBank.bytes','wb') as f1:
                                    f1.write(strin)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbySound.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00'+id_mod + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1:
                                strin = strin.replace(b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                strin = strin.replace(b'\x00'+id_mod+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbySound.bytes','wb') as f1:
                                    f1.write(strin)
                except Exception as bug:
                    print(bug)
                    print(Fore.RED+Style.BRIGHT+'Không Mod Sound'+Style.RESET_ALL)
            #-----------------------------------------------Mod Skill Mark------------------------------------------------------------#
                print('Mod Skill Mark')
                list_du_kien_mod_born=[]
                list_skill_mark=[]
                try:
                    
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Skill/skillmark.bytes','rb') as f:
                        a=f.read()
                        t=b'prefab_skill_effects/hero_skill_effects/'+skinid[:3]+b'_'
                        if b's/'+skinid[:3]+b'_' in a or b'S/'+skinid[:3]+b'_' in a:
                            a=skillmark(a,skinid)
                            p=a.find(t)
                            while p!=-1:
                                p2=a.find(b'\x00',p)
                                code=a[p:p2]
                                if skinid in code:
                                    print(code)
                                    list_du_kien_mod_born.append(code)
                                p=a.find(t,p2)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Skill/skillmark.bytes','wb') as f1:
                            f1.write(a)
                except:
                    print(Fore.RED+Style.BRIGHT+'Không Mod skillmark'+Style.RESET_ALL)
            #-----------------------------------------------Mod Effect------------------------------------------------------------#
                if True:
                    ca=ca+tat+'\n'
                    if hieu_ung == b'\x8f':
                        du_kien_mod_born=b''
                        
                        with open(f'./Pmin_Sources/Resources/1.58.1/AssetRefs/Hero/{decompress[:3]}_AssetRef.bytes','rb') as asef:
                            check_asef=fix_ef(mod_ef_sound2(decompress_(asef.read()),decompress,skinid),skinid).lower()
                            p=check_asef.find(b'skinsubset')
                            if p!=-1:
                                check_asef=check_asef[:p]
                        for filez in listdir(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}'):
                            if filez=='skill' or filez=='Skill':
                                for file in listdir('./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/skill/'.format(decompress)):
                                    if True:
                                        try:
                                            with open('./Pmin_Sources/check/{}/{}'.format(skinid.decode(),file),'rb') as f:
                                                strin = f.read()
                                                print(Fore.GREEN+Style.BRIGHT+'File Có Skill Ẩn: '+file)
                                                strin=mod_ef_sound2(strin,decompress,skinid)
                                                check_skill_an=True
                                                list_skill_an.append(file)
                                                if HD_e:
                                                    p=strin.find(b'<String name="resourceName')
                                                    while p!=-1:
                                                        p2=strin.find(b'"',p+len('<String name="resourceName2" value="'))
                                                        if b'.prefab' not in strin[p:p2+1] and b'value=""' not in strin[p:p2+1]:
                                                            print('HD_E')
                                                            print(strin[p:p2+1])
                                                            strin=strin.replace(strin[p:p2+1],strin[p:p2]+b'.prefab"',1)
                                                        p=strin.find(b'<String name="resourceName',p2)
                                        except:
                                            with open(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','rb') as f:
                                                strin = f.read()
                                                strin=decompress_(strin,ZSTD_DICT)
                                                strin=mod_ef_sound(strin,decompress,skinid,file,folder_mod)
                                                if veres_rt:
                                                    strin=strin.replace(b'prefab_skill_effects/hero_skill_effects/520_Veres/52007/',b'prefab_skill_effects/component_effects/52007/'+skinid_veres+b'/')
                                                if phu_kien and skinid==b'54004':
                                                    strin=strin.replace(b'hero_skill_effects/540_Bright/54004/5401_Bright_God',b'component_effects/54004/540040'+str(int(skinid_phu_kien[9:].decode())-1).encode('utf-8')+b'/5401_Bright_God')
                                                pos = strin.find(b'<int name="skinId" value="'+skinid)
                                                if pos!=-1:
                                                    print(Fore.GREEN+Style.BRIGHT+'File Có Skill Ẩn: '+file)
                                                    check_skill_an=True
                                                    list_skill_an.append(file)
                                                    if check_skill_an and False:
                                                        strin=fix_ef_pro_vip(strin,skinid)
                                                def xoa_skinid_no_need(xml_bytes, skinid):
                                                    for i in range(1, 25):
                                                        i_bytes = b'0' * (2 - len(str(i))) + str(i).encode('utf-8')
                                                        t = b'<int name="skinId" value="' + skinid[:3] + i_bytes
                                                        t_next = b'<int name="skinId" value="' + skinid[:3] + b'91'
                                                        t_0 = b'<int name="skinId" value="' + skinid[:3] + b'00'
                                                        if t in xml_bytes and t_0 not in xml_bytes and skinid[:3] + i_bytes != skinid:
                                                            xml_bytes = xml_bytes.replace(t, t_next)
                                                    return xml_bytes
                                                if skinid[:3]==b'190' and file.lower() in ['s1b1.xml','s1b2.xml','s1b3.xml']:
                                                    strin=xoa_skinid_no_need(strin,skinid)
                                                if HD_e:
                                                    p=strin.find(b'<String name="resourceName')
                                                    while p!=-1:
                                                        p2=strin.find(b'"',p+len('<String name="resourceName2" value="'))
                                                        if b'.prefab' not in strin[p:p2+1] and b'value=""' not in strin[p:p2+1]:
                                                            print('HD_E')
                                                            print(strin[p:p2+1])
                                                            strin=strin.replace(strin[p:p2+1],strin[p:p2]+b'.prefab"',1)
                                                        p=strin.find(b'<String name="resourceName',p2)
                                        if KatakanaXinhGai and skinid not in [b'11620',b'13111',b'16707']:
                                            pos = strin.find( b'<Event eventName="PlayHeroSoundTick')
                                            sound_id = str(int(skinid[3:].decode())).encode()
                                            while pos != -1:
                                                posid = strin.find(b'<String name="eventName" value="',pos)
                                                posid2 = strin.find(b'" refParamName="" useRefParam="false" />',posid)
                                                code = strin[posid:posid2]
                                                posid3 = code.find(b'_Skin'+sound_id)
                                                if posid3 !=-1:
                                                    strin = strin
                                                else:
                                                    if skinid!=b'13006':
                                                        strin = strin.replace(code,code+b'_skin'+sound_id,1)
                                                    else:
                                                        strin=strin.replace(code,code+b'_skin5')
                                                pos = strin.find( b'<Event eventName="PlayHeroSoundTick',posid)
                                            strin=fix_sound(strin,sound_id)
                                            anti=strin
                                            strin=fix_ef(strin,skinid)
                                        #fix ef mặc định
                                        import re
                                        if skinid ==b'19015':
                                            strin=strin.replace(b'\r\n      <SkinOrAvatarList id="19015" />',b'')
                                        elif skinid[:3] == b'544' and file=='A4B1.xml':
                                            strin=strin.replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/54402/Painter_Atk4_blue',b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_blue').replace(b'prefab_skill_effects/hero_skill_effects/544_Painter/54402/Painter_Atk4_red',b'prefab_skill_effects/hero_skill_effects/544_Painter/Painter_Atk4_red')
                                        elif skinid[:3]==b'521' and skinid!='52108' and file in ['S1B3.xml','S1B4.xml']:
                                            strin=strin.replace(b'Florentino_spell01_bullet03_2"',b'Florentino_spell01_bullet03"').replace(b'Florentino_spell01_bullet03_fade_2"',b'Florentino_spell01_bullet03_fade"').replace(b'Florentino_spell01_bullet03_2_e"',b'Florentino_spell01_bullet03_e"').replace(b'Florentino_spell01_buff01_2"',b'Florentino_spell01_buff01"')
                                            strin=strin.replace(b'Florentino_spell01_bullet03_3"',b'Florentino_spell01_bullet03"').replace(b'Florentino_spell01_bullet03_fade_3"',b'Florentino_spell01_bullet03_fade"').replace(b'Florentino_spell01_bullet03_3_e"',b'Florentino_spell01_bullet03_e"').replace(b'Florentino_spell01_buff01_3"',b'Florentino_spell01_buff01"')
                                        elif skinid[:3]==b'524' and file =='A1E9.xml':
                                            strin=strin.replace(b'hero_skill_effects/524_Capheny/'+skinid,b'hero_skill_effects/524_Capheny')
                                        elif skinid[:3] == b'537':
                                            strin = re.sub(
                                                rb'prefab_skill_effects/hero_skill_effects/537_Trip/' + skinid + rb'/Trip_attack_spell01_Indicator',
                                                rb'prefab_skill_effects/hero_skill_effects/537_Trip/53703/Trip_attack_spell01_Indicator',
                                                strin, flags=re.IGNORECASE)

                                        elif skinid == b'53802':
                                            strin = re.sub(
                                                rb'prefab_skill_effects/hero_skill_effects/538_Iggy/53802/Iggy_Spell3_Circle_01_E',
                                                rb'prefab_skill_effects/hero_skill_effects/538_Iggy/Iggy_Spell3_Circle_01_E',
                                                strin, flags=re.IGNORECASE)

                                        elif skinid == b'13504':
                                            strin = re.sub(
                                                rb'prefab_skill_effects/hero_skill_effects/135_xiangyu/13504/135_spell_02_blue',
                                                rb'prefab_skill_effects/hero_skill_effects/135_xiangyu/135_spell_02_blue',
                                                strin, flags=re.IGNORECASE)
                                            strin = re.sub(
                                                rb'prefab_skill_effects/hero_skill_effects/135_xiangyu/13504/135_spell_02_red',
                                                rb'prefab_skill_effects/hero_skill_effects/135_xiangyu/135_spell_02_red',
                                                strin, flags=re.IGNORECASE)

                                        elif skinid == b'18004':
                                            strin = re.sub(
                                                rb'prefab_skill_effects/hero_skill_effects/180_nezha/18004/nezha_attack03_spell05',
                                                rb'prefab_skill_effects/hero_skill_effects/180_nezha/nezha_attack03_spell05',
                                                strin, flags=re.IGNORECASE)
                                            strin = re.sub(
                                                rb'prefab_skill_effects/hero_skill_effects/180_nezha/18004/nezha_loop_06',
                                                rb'prefab_skill_effects/hero_skill_effects/180_nezha/nezha_loop_06',
                                                strin, flags=re.IGNORECASE)

                                        elif skinid[:3] == b'173':
                                            strin = re.sub(
                                                rb"prefab_skill_effects/hero_skill_effects/173_liyuanfang/" + skinid + rb"/Liyuanfang_buff01_spell03",
                                                rb"prefab_skill_effects/hero_skill_effects/173_liyuanfang/Liyuanfang_buff01_spell03",
                                                strin, flags=re.IGNORECASE)

                                        elif skinid[:3] == b'148':
                                            strin = re.sub(
                                                rb"prefab_skill_effects/hero_skill_effects/148_jiangziya/" + skinid + rb"/jiangziya_yujing_spell03_e",
                                                rb"prefab_skill_effects/hero_skill_effects/148_jiangziya/jiangziya_yujing_spell03_e",
                                                strin, flags=re.IGNORECASE)

                                        elif skinid == b'52302':
                                            strin = re.sub(
                                                rb"prefab_skill_effects/hero_skill_effects/523_Darcy/52302/Darcy_spell03_atk02_e",
                                                rb"prefab_skill_effects/hero_skill_effects/523_Darcy/Darcy_spell03_atk02_e",
                                                strin, flags=re.IGNORECASE)
                                            strin = re.sub(
                                                rb"prefab_skill_effects/hero_skill_effects/523_Darcy/52302/Darcy_spell03_buff02",
                                                rb"prefab_skill_effects/hero_skill_effects/523_Darcy/Darcy_spell03_buff02",
                                                strin, flags=re.IGNORECASE)

                                        elif skinid[:3] == b'140':
                                            file_lower = file.lower()
                                            special_files = [
                                                "ts2e6.xml", "ts2e1.xml", "ts1e2.xml", "ta1e1.xml", "ta1.xml",
                                                "s2b1.xml", "s1e1.xml", "s1b1.xml", "p1e7.xml", "p1.xml", "a1e1.xml"
                                            ]

                                            if file_lower in special_files:
                                                strin = strin.replace(b'/' + skinid + b'/', b'/')

                                            elif file_lower == 'ts1.xml':
                                                strin = re.sub(
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/' + skinid + rb'/guanyu_attack01_spell03',
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/guanyu_attack01_spell03',
                                                    strin, flags=re.IGNORECASE)

                                            elif file_lower == 'ts2.xml':
                                                strin = re.sub(
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/' + skinid + rb'/guanyu_attack02_spell05',
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/guanyu_attack02_spell05',
                                                    strin, flags=re.IGNORECASE)

                                            elif file_lower in ['tu1.xml', 'u1.xml']:
                                                strin = re.sub(
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/' + skinid + rb'/guanyu_attack03_spell03',
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/guanyu_attack03_spell03',
                                                    strin, flags=re.IGNORECASE)

                                            elif file_lower in ['tu1b1.xml', 'tu1b2.xml', 'tu1b3.xml', 'tu1b4.xml']:
                                                strin = re.sub(
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/' + skinid + rb'/guanyu_attack03_spell02',
                                                    rb'prefab_skill_effects/hero_skill_effects/140_guanyu/guanyu_attack03_spell02',
                                                    strin, flags=re.IGNORECASE)

                                        #xoa dong thua thai
                                        
                                        #   
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:
                                            f1.write(compress_(xoa_thua_thai(strin)))
                                    if ('e' in file.lower() and len(list_du_kien_mod_born)==0) or (skinid[:3]!=b'524' and file in ['A1E1.xml','A1e1.xml','a1e1.xml']) or (skinid[:3]==b'524' and file in ['A1E6.xml','A1e6.xml','a1e6.xml']):
                                        for ef in [b'Prefab_Skill_Effects',b'Prefab_Skill_Effects'.lower()]:
                                            p=strin.find(ef)
                                            while p!=-1:
                                                p2=strin.find(b'"',p)
                                                du_kien_mod_born=strin[p:p2].lower()
                                                list_du_kien_mod_born.append(du_kien_mod_born)
                                                print('born')
                                                print(file, du_kien_mod_born)
                                                p=strin.find(ef,p2)
                                    if b'Prefab_Skill_Effects'.lower() in strin.lower():
                                        def split_code_back2(a):
                                            split_code=[]
                                            p=a.find(b'    <Track trackName=')
                                            while p!=-1:
                                                code=a[p:a.find(b'    <Track trackName=',p+10)].replace(b'  </Action>\r\n</Project',b'')
                                                split_code.append(code)
                                                p=a.find(b'    <Track trackName=',p+10)
                                            return split_code
                                        
                                        def extract_guid_after_id(xml_bytes: bytes) -> bytes:
                                            if b'<Project>' in xml_bytes:
                                                xml_text = xml_bytes.decode('utf-8')

                                                pattern = re.compile(r'id="([^"]+)"(?:\s+guid="([^"]+)")?')

                                                results = []

                                                for match in pattern.finditer(xml_text):
                                                    id_val = match.group(1)
                                                    guid_val = match.group(2)

                                                    id_str = f'id="{id_val}"'

                                                    if guid_val:
                                                        snippet = xml_text[match.start():match.end()]
                                                        after_id = snippet[len(id_str):].lstrip()

                                                        if after_id.startswith(f'guid="{guid_val}"'):
                                                            results.append(f'{id_str} guid="{guid_val}"')
                                                            results.append(f'guid="{guid_val}"')
                                                            split_code = split_code_back2(xml_bytes)
                                                            for i in range(len(split_code)):
                                                                p=re.search(rb'guid="'+guid_val.encode('utf-8')+rb'" enabled="',split_code[i])
                                                                if p and id_str != f'id="{i}"':
                                                                    xml_bytes=xml_bytes.replace(f'{id_str} guid="{guid_val}"'.encode('utf-8'),f'id="{i}" guid="{guid_val}"'.encode('utf-8'))
                                                            print(results)

                                            return xml_bytes
                                        #print(file, extract_guid_after_id(strin).decode('utf-8'),end="\n\n")
                                        for code in split_code_back2(strin):
                                            mod_all = b'''    <Track trackName="PMIN" eventType="GetHolidayResourcePathTick" guid="Mod By: Lyna TV" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="GetHolidayResourcePathTick" time="0.000" isDuration="false" guid="Mod By: Pmin Mod">
        <String name="holidayResourcePathPrefix" value="EFFECT
        <String name="outPathParamName" value="CHECK_CODE" useRefParam="false" />
        <String name="outSoundEventParamName" useRefParam="false" />
      </Event>
    </Track>
'''
                                            code_goc=code
                                            p=re.search(rb'prefab_skill_effects.*?>',code,re.IGNORECASE)
                                            if p and decompress.encode('utf-8').lower() in code.lower() and b'BattleUI' not in code and b'enabled="true"' in code and (b'ChangeActorMeshDuration' in code or b'ChangeActorMeshTick' in code or b'TriggerParticle' in code or b'TriggerParticleTick' in code):
                                                ef = p.group()
                                                match = re.search(rb'([^/"]+)"', ef, re.IGNORECASE)
                                                match2 = re.search(rb'eventType="([^"]+)"', code, re.IGNORECASE)
                                                if match:
                                                    nhan_dang = match.group(1)  # Output: zhaoyunn_hurt01
                                                else:
                                                    nhan_dang = b''
                                                try:
                                                    with open(f'a.xml','rb') as f:
                                                        code_sua_getholi = f.read()
                                                except:
                                                    code_sua_getholi=b''
                                                if match2.group(1) not in code_sua_getholi:
                                                    with open(f'a.xml','wb') as f2:
                                                        f2.write(match2.group(1)+b'\r\b'+code_sua_getholi)
                                                check_ef=b'" refParamName="'+nhan_dang+b'" useRefParam="true" />'
                                                code=code.replace(ef,check_ef)
                                                con = re.search(rb'<Condition.*?<Event\s*eventName',code_goc,re.IGNORECASE | re.DOTALL)
                                                if con:
                                                    condition = con.group()
                                                else:
                                                    condition=b'<Event eventName'
                                                
                                                mod_for_skin = mod_all.replace(b'<Event eventName',condition).replace(b'EFFECT',ef).replace(b'CHECK_CODE',nhan_dang)
                                                strin=strin.replace(code_goc, mod_for_skin+code)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:
                                            f1.write(compress_(xoa_thua_thai(extract_guid_after_id(strin))))
                                    if may_yeu_mod and not HD_e and False:
                                        for ef in [b'Prefab_Skill_Effects',b'Prefab_Skill_Effects'.lower()]:
                                            p=strin.find(ef)
                                            while p!=-1:
                                                p2=strin.find(b'"',p)
                                                du_kien_mod_born=strin[p:p2].lower()
                                                if strin[p:p2].lower().replace(b'.prefab',b'') not in check_asef and b'pmin' not in strin[p:p2].lower() and skinid in strin[p:p2].lower():
                                                    print('born')
                                                    print(du_kien_mod_born)
                                                    list_du_kien_mod_born.append(du_kien_mod_born)
                                                p=strin.find(ef,p2)
                                    list_du_kien_mod_born=list(set(list_du_kien_mod_born))
                                    if DeAllSkin:
                                        ListRandom=['1','2','3','4','5','6','7','8','9','P','M','I','N','O','D','G','A','0']
                                        import random
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','rb') as f1:
                                            text=f1.read()
                                            if b'<String name="resourceName" value="' in text:
                                                p=text.find(b'<String name="resourceName')
                                                while p!=-1:
                                                    p2=text.find(b'\r\n',p)
                                                    code=text[p:p2]
                                                    Dau_resources=code[:code.find(b'" value="')]
                                                    ef=code[code.find(b'" value="')+9:][:code[code.find(b'" value="')+9:].find(b'"')]
                                                    codeNhanDang = (''.join(str(random.choice(ListRandom)) for _ in range(16))).encode('utf-8')
                                                    code_chinh_sua=Dau_resources+b'" value="" refParamName="'+codeNhanDang+b'" useRefParam="true" />'
                                                    getHoliday=b'    <Track trackName="" eventType="GetHolidayResourcePathTick" guid="Test" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="GetHolidayResourcePathTick" isDuration="false" guid="Zalo_0357514770">\r\n        <String name="holidayResourcePathPrefix" value="code_ef" refParamName="" useRefParam="false" />\r\n        <String name="outPathParamName" value="code_nhan_dang" refParamName="" useRefParam="false" />\r\n        <String name="outSoundEventParamName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>'.replace(b'code_nhan_dang',codeNhanDang).replace(b'code_ef',ef)
                                                    if ef!=b'':
                                                        text=text.replace(code,code_chinh_sua,1)
                                                        text=text.replace(b'  </Action>',getHoliday)
                                                    p=text.find(b'<String name="resourceName',p2)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:f1.write(text)
                                if check_skill_an:
                                    ten_de_vao_skill_an=ten_de_vao_skill_an+decompress+'\n'
                                    for i in list_skill_an:
                                        ten_de_vao_skill_an=ten_de_vao_skill_an+'\t'+i+'\n'
                            else:
                                for file in listdir(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/{filez}'):
                                    with open(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/{filez}/{file}','rb') as f:
                                        strin = f.read()
                                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/{filez}/{file}','wb') as f1:
                                                f1.write(strin)
                    else:
                        for file in listdir('./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/skill/'.format(decompress)):
                            if '.xml' in file:
                                with open(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','rb') as f:
                                    strin = f.read()
                                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:
                                        f1.write(strin)
                #--------------Mod Born--------------------
                if hieu_ung == b'\x8f' and not DeAllSkin and False:
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Born.xml','rb') as f1:
                        strin=f1.read()
                        check=b'    <Track trackName="BORN_ID_SKIN" eventType="CheckHeroIdTick" guid="Mod_by_PminMod_Fix_Lag_ID_SKIN" enabled="true" r="0.000" g="0.000" b="0.000" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" guid="Mod_Vip">\r\n      <TemplateObject name="targetId" id="0" objectName="self"/>\r\n        <int name="heroId" value="ID_SKIN"/>\r\n      </Event>\r\n    </Track>\r\n'
                        strin=strin.replace(b'  </Action>\r\n</Project>',check.replace(b'ID_SKIN',skinid[:3])+b'  </Action>\r\n</Project>',1)
                        ef=b'    <Track trackName="PminMod" eventType="TriggerParticleTick" guid="I LOVE YOU" enabled="true" r="0.000" g="0.000" b="0.000" stopAfterLastEvent="true" SkinAvatarFilterType="9">\r\n      <Condition id="1" guid="Mod_by_PminMod_Fix_Lag_ID_SKIN" status="true" />\r\n      <Event eventName="TriggerParticleTick" time="0.000" length="0.001" guid="866871db-f8fd-4577-8cb7-e0ee803ade3f">\r\n        <TemplateObject name="targetId" id="1" objectName="target"/>\r\n        <String name="resourceName" value="EFFECT"/>\r\n      </Event>\r\n    </Track>\r\n'
                        for du_kien_mod_born in list_du_kien_mod_born:
                            strin=strin.replace(b'  </Action>\r\n</Project>',ef.replace(b'ID_SKIN',skinid[:3]).replace(b'EFFECT', du_kien_mod_born)+b'  </Action>\r\n</Project>')
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Born.xml','wb') as f1:
                        f1.write(strin)
            #-----------------------------------------------Mod heroSkin------------------------------------------------------------#
                try:
                    if True:
                        id_2_so = bytes(str(int(skinid[3:].decode())),'utf-8')
                        id_0 = skinid[:3]+b'00';id_0=id_0.decode();id_0 = hex(int(id_0))[2:]
                        if len(id_0)==3:
                            id_0='0'+id_0
                        id_0 = bytes.fromhex(id_0);id_0 = id_0[1:]+id_0[:1];id_mod = skinid;id_mod=id_mod.decode();id_mod = hex(int(id_mod))[2:]
                        if len(id_mod)==3:
                            id_mod='0'+id_mod
                        id_mod = bytes.fromhex(id_mod);id_mod= id_mod[1:]+id_mod[:1];hero_actor = hex(int(skinid[:3].decode()))[2:]
                        if len(hero_actor)%2 ==1:
                            hero_actor='0'+hero_actor
                        hero_actor=bytes.fromhex(hero_actor);hero_actor = hero_actor[1:]+hero_actor[:1]
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(id_mod+b'\x00\x00'+hero_actor)
                            if pos!=-1:
                                actor_mod = strin[pos-4:pos-2];actor_mod = actor_mod[1:]+actor_mod[:1];actor_mod=actor_mod.hex();actor_mod=int(actor_mod,16);actor_mod=strin[pos-4:pos+actor_mod]
                                pos = strin.find(id_0+b'\x00\x00'+hero_actor)
                                if pos !=-1:
                                    actor_0 = strin[pos-4:pos-2];actor_0 = actor_0[1:]+actor_0[:1];actor_0=actor_0.hex();actor_0=int(actor_0,16);actor_0=strin[pos-4:pos+actor_0]
                                    if skinid==b'16707':
                                        actor_mod=actor_mod[:4]+actor_0[4:10]+actor_mod[10:36]+b'\x00'+actor_mod[37:]
                                        actor_mod=actor_mod.replace(b'\x07\x00\x00\x00301677',b'\x07\x00\x00\x00301670',1)
                                        actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_16707\x2ejpg',b'\x12\x00\x00\x00Share_16707_2\x2ejpg').replace(b'\x0a\x00\x00\x0016707\x2ejpg',b'\x0c\x00\x00\x0016707_2\x2ejpg').replace(b'\x0b\x00\x00\x00301677\x2ejpg',b'\x0d\x00\x00\x00301677_2\x2ejpg').replace(b'\x0f\x00\x00\x00301677head\x2ejpg',b'\x11\x00\x00\x00301677_2head\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x2d\x00\x00\x00\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x2f\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d')
                                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                        strin = strin.replace(actor_0,actor_mod,1)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif skinid==b'10620':
                                        actor_mod=actor_mod[:4]+actor_0[4:10]+actor_mod[10:36]+b'\x00'+actor_mod[37:]
                                        actor_mod=actor_mod.replace(b'\x08\x00\x00\x003010620',b'\x07\x00\x00\x00301060',1)
                                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                        strin = strin.replace(actor_0,actor_mod,1)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif skinid==b'13118':
                                        actor_mod=actor_mod[:4]+actor_0[4:10]+actor_mod[10:36]+b'\x00'+actor_mod[37:]
                                        actor_mod=actor_mod.replace(b'\x0c\x00\x00\x003013118',b'\x0b\x00\x00\x00301310',1)
                                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                        strin = strin.replace(actor_0,actor_mod,1)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif skinid==b'13311':
                                        actor_mod=actor_mod[:4]+actor_0[4:10]+actor_mod[10:36]+b'\x00'+actor_mod[37:]
                                        actor_mod=actor_mod.replace(b'\x08\x00\x00\x003013311',b'\x07\x00\x00\x00301330',1)
                                        actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_11620\x2ejpg',b'\x12\x00\x00\x00Share_11620_2\x2ejpg').replace(b'\x0a\x00\x00\x0011620\x2ejpg',b'\x0c\x00\x00\x0011620_2\x2ejpg').replace(b'\x0c\x00\x00\x003011620\x2ejpg',b'\x0e\x00\x00\x003011620_2\x2ejpg').replace(b'\x10\x00\x00\x003011620head\x2ejpg',b'\x12\x00\x00\x003011620head_2\x2ejpg')
                                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                        strin = strin.replace(actor_0,actor_mod,1)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif skinid==b'15412':
                                        actor_mod=actor_mod[:4]+actor_0[4:10]+actor_mod[10:36]+b'\x00'+actor_mod[37:]
                                        actor_mod=actor_mod.replace(b'\x08\x00\x00\x003015412',b'\x07\x00\x00\x00301540',1)
                                        actor_mod=actor_mod.replace(b'\x12\x00\x00\x003015412_B43_1',b'\x0c\x00\x00\x003015412',1)
                                        actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                        strin = strin.replace(actor_0,actor_mod,1)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif len(id_2_so)==2 and skinid[:3]!=b'190':
                                        pos = actor_0.find(actor_0[63:])
                                        posid = actor_0.find(b'Share_'+hero_name[:3]+b'00',pos)
                                        khung_0 = actor_0[pos:posid]
                                        id_0 = actor_0[4:][:2]
                                        pos = actor_mod.find(actor_mod[63:])
                                        posid = actor_mod.find(b'Share_'+skinid,pos)
                                        khung_mod = actor_mod[pos:posid]
                                        re_mod = actor_mod.replace(khung_mod,khung_0)
                                        re_mod = re_mod[:4]+id_0+re_mod[6:]
                                        re_mod = re_mod[:36]+b'\x00'+re_mod[37:]
                                        dau_mod = int(len(re_mod)-4)
                                        dau_mod = hex(dau_mod)[2:]
                                        if len(dau_mod) == 3:
                                            dau_mod = '0'+dau_mod
                                        dau_mod = bytes.fromhex(dau_mod)
                                        re_mod = dau_mod[1:]+dau_mod[:1] + re_mod[2:]
                                        strin = strin.replace(actor_0,re_mod)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif len(id_2_so)==1 and skinid[:3]!=b'190':
                                        pos = actor_mod.find(id_mod+b'\x00\x00'+hero_actor)
                                        posid = actor_mod.find(b'Share_'+skinid)
                                        actor_mod = actor_mod.replace(actor_mod[pos:posid],actor_mod[pos:posid].replace(b'30'+skinid[:3]+id_2_so,b'30'+skinid[:3]+b'0'))
                                        re_mod = actor_0[:16]+actor_mod[16:][:20]+b'\x00'+actor_mod[37:]
                                        dau_mod = int(len(re_mod)-4)
                                        dau_mod = hex(dau_mod)[2:]
                                        if len(dau_mod) == 3:
                                            dau_mod = '0'+dau_mod
                                        dau_mod = bytes.fromhex(dau_mod)
                                        re_mod = dau_mod[1:]+dau_mod[:1] + re_mod[2:]
                                        strin = strin.replace(actor_0,re_mod)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    elif skinid[:3]==b'190':
                                        actor_02=actor_mod
                                        actor_02=actor_02.replace(dec_to_hex(int(skinid.decode()))+b'\x00\x00'+dec_to_hex(int(skinid.decode()[:3])),dec_to_hex(int(skinid.decode()[:3]+'00'))+b'\x00\x00'+dec_to_hex(int(skinid.decode()[:3])))
                                        if len(str(int(skinid[3:].decode())))==2:
                                            actor_02=dec_to_hex(hex_to_dec(actor_02[:1])-1)+actor_02[1:]
                                            actor_02=actor_02.replace(b'\x08\x00\x00\x00\x33\x30',b'\x07\x00\x00\x00\x33\x30')
                                        actor_02=actor_02.replace(b'\x33\x30'+skinid[:3]+str(int(skinid[3:].decode())).encode('utf-8'),b'\x33\x30'+skinid[:3]+b'0',1)
                                        actor_02=actor_02[:36]+b'\x00'+actor_02[37:]
                                        strin = strin.replace(actor_0,actor_02)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                                    else:
                                        pass
                except Exception as bug:
                    print(bug)
                    print('\n\t\033[0m          [   \033[1;31mKhông Mod Heroskin Mặc Định\033[0m    ]')
                skin_phu_bac_a=find_skin_A(skinid)
            #-----------------------------------------------Mod Skin Phụ------------------------------------------------------------#
                print('Mod Skin Phụ')
                try:
                    #for nnn in skin_phu_bac_a:
                    for nnn in range(1,30):
                        #nnn=int(nnn.decode()[3:])-1
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','rb') as f:
                            strin = f.read()
                            hero_actor=dec_to_hex(int(skinid[:3].decode()))
                            id_mod=dec_to_hex(int(skinid.decode()))
                            pos = strin.find(id_mod+b'\x00\x00'+hero_actor)
                            if pos!=-1:
                                actor_mod = strin[pos-4:pos+hex_to_dec(strin[pos-4:pos-2])]
                                if skinid==b'16707':
                                    actor_mod=actor_mod.replace(b'\x07\x00\x00\x00301677',b'\x09\x00\x00\x00301677_2',1)
                                    actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_16707\x2ejpg',b'\x12\x00\x00\x00Share_16707_2\x2ejpg').replace(b'\x0a\x00\x00\x0016707\x2ejpg',b'\x0c\x00\x00\x0016707_2\x2ejpg').replace(b'\x0b\x00\x00\x00301677\x2ejpg',b'\x0d\x00\x00\x00301677_2\x2ejpg').replace(b'\x0f\x00\x00\x00301677head\x2ejpg',b'\x11\x00\x00\x00301677_2head\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x2d\x00\x00\x00\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x2f\x42\x47\x5f\x77\x75\x6b\x6f\x6e\x67\x6a\x75\x65\x78\x69\x6e\x67\x32\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d')
                                    actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                if skinid==b'13311':
                                    actor_mod=actor_mod.replace(b'\x08\x00\x00\x003013311',b'\x0a\x00\x00\x003013311_2',1)
                                    actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_13311\x2ejpg',b'\x12\x00\x00\x00Share_13311_2\x2ejpg').replace(b'\x0a\x00\x00\x0013311\x2ejpg',b'\x0c\x00\x00\x0013311_2\x2ejpg').replace(b'\x0c\x00\x00\x003013311\x2ejpg',b'\x0e\x00\x00\x003013311_2\x2ejpg').replace(b'\x10\x00\x00\x003013311head\x2ejpg',b'\x12\x00\x00\x003013311head_2\x2ejpg').replace(b'\x25\x00\x00\x00\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x2f\x42\x47\x5f\x43\x6f\x6d\x6d\x6f\x6e\x73\x5f\x30\x31\x5f\x50\x6c\x61\x74\x66\x6f\x72\x6d',b'\x33\x00\x00\x00\x42\x47\x5f\x44\x69\x52\x65\x6e\x4a\x69\x65\x5f\x31\x33\x33\x31\x32\x5f\x54\x33\x2f\x42\x47\x5f\x79\x69\x6e\x79\x69\x6e\x67\x7a\x68\x69\x73\x68\x6f\x75\x5f\x30\x31\x5f\x70\x6c\x61\x74\x66\x6f\x72\x6d')
                                    actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                if skinid==b'11620':
                                    actor_mod=actor_mod.replace(b'\x08\x00\x00\x003011620',b'\x0a\x00\x00\x003011620_2',1)
                                    actor_mod=actor_mod.replace(b'\x10\x00\x00\x00Share_11620\x2ejpg',b'\x12\x00\x00\x00Share_11620_2\x2ejpg').replace(b'\x0a\x00\x00\x0011620\x2ejpg',b'\x0c\x00\x00\x0011620_2\x2ejpg').replace(b'\x0c\x00\x00\x003011620\x2ejpg',b'\x0e\x00\x00\x003011620_2\x2ejpg').replace(b'\x10\x00\x00\x003011620head\x2ejpg',b'\x12\x00\x00\x003011620head_2\x2ejpg')
                                    actor_mod=dec_to_hex(len(actor_mod)-4)+actor_mod[2:]
                                id_2=dec_to_hex(int(skinid[:3].decode())*100+nnn)
                                pos = strin.find(id_2+b'\x00\x00'+hero_actor)
                                if pos !=-1:
                                    actor_2 = strin[pos-4:pos+hex_to_dec(strin[pos-4:pos-2])]
                                    re_2 = actor_mod[:4]+id_2+actor_mod[6:][:30]+dec_to_hex(nnn)+actor_mod[37:]
                                    if re_2!=b'' and actor_2!=b'' and nnn!=int(skinid[3:].decode()):
                                        strin=strin.replace(actor_2,re_2)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f1:
                                            f1.write(strin)
                        try:
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','rb') as f:
                                strin = f.read()
                                hero_actor=dec_to_hex(int(skinid[:3].decode()))
                                pos = strin.find(id_2+b'\x00\x00'+hero_actor)
                                if pos !=-1:
                                    hs_2 = strin[pos-4:pos+hex_to_dec(strin[pos-4:pos-2])]
                                    pos = strin.find(id_mod+b'\x00\x00'+hero_actor)
                                    if pos!=-1:
                                        hs_mod = strin[pos-4:pos+hex_to_dec(strin[pos-4:pos-2])]
                                        if skinid==b'13311' or skinid==b'11620':
                                            with open(f'./Pmin_Sources/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','rb') as f:
                                                strin2 = decompress_(f.read(),ZSTD_DICT)
                                            pos = strin2.find(b'\x43\x41\x00\x00\xA7')
                                            hs_mod = strin2[pos-4:pos+hex_to_dec(strin2[pos-4:pos-2])]
                                            hs_mod=hs_mod.replace(b'\x43\x41\x00\x00\xA7',b'\xFF\x33\x00\x00\x85')
                                            hs_mod=hs_mod[:36]+b'\x0B'+hs_mod[37:]
                                            hs_mod=hs_mod.replace(b'Awake_Label_1',b'Awake_Label_5')
                                        if skinid==b'16707':
                                            hs_mod=hs_mod.replace(b'Awake_Label_1',b'Awake_Label_5')

                                    else:
                                        hs_mod=b'\x2C\x01\x00\x00PMINMOD\x00\x00\x14\x00\x00\x00\x42\x46\x42\x37\x36\x35\x44\x41\x30\x33\x33\x42\x39\x41\x32\x32\x5F\x23\x23\x00\x0B\x00\x00\x00\x14\x00\x00\x00\x33\x39\x36\x37\x36\x31\x39\x30\x34\x42\x32\x36\x45\x44\x45\x30\x5F\x23\x23\x00\x14\x00\x00\x00\x34\x42\x42\x32\x36\x42\x33\x36\x45\x32\x39\x30\x39\x31\x30\x37\x5F\x23\x23\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\x00\x00\x00\x4C\x61\x62\x65\x6C\x5F\x53\x53\x53\x5F\x4C\x69\x6D\x69\x74\x65\x64\x2E\x70\x6E\x67\x00\x03\x00\x14\x00\x00\x00\x42\x46\x42\x42\x35\x39\x41\x35\x44\x37\x45\x36\x32\x33\x43\x36\x5F\x23\x23\x00\x00\x48\x0B\x00\x00\x00\x00\x00\x00\x00\x00\x48\x0B\x00\x00\x00\x00\x1C\x00\x00\x00\x00\xD2\x0A\x3D\x00\x00\x3F\xFC\x01\x00\x40\xFC\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x00\x00\x00\x32\x30\x32\x31\x30\x32\x30\x38\x30\x30\x30\x30\x30\x30\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCF\x84\x01\x00\x01\x01\x00\x00\x06\x1C\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
                                        t=dec_to_hex(int(skinid.decode()))+b'\x00\x00'+dec_to_hex(int(skinid.decode()[:3]))
                                        if len(t)==5:
                                            t+=b'\x00'
                                        hs_mod=hs_mod.replace(b'PMINMOD',t)
                                hs_mod = hs_mod[:4]+hs_2[4:][:2]+hs_mod[6:]
                                hs_mod = hs_mod[:36]+hs_2[36:][:1]+hs_mod[37:]
                            strin = strin.replace(hs_2,hs_mod)
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','wb') as f1:
                                f1.write(strin)
                        except Exception as bug:
                            print(bug)          
                            pass
                except Exception as bug:
                    print(bug)          
                    pass
            #-----------------------------------------------Mod Infos Skin Mặc Định------------------------------------------------------------#
                print('Mod Infos Skin Mặc Định')
                for file in listdir('./Pmin_Sources/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}/'.format(decompress)):
                    with open(f'./Pmin_Sources/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{decompress}/{file}','rb') as f:
                        a=f.read()
                        check_file3=False
                        if len(file) == len(decompress)+len('_actorinfo.bytes'):a=decompress_(a,ZSTD_DICT);file2=file
                        if 'trap' in file or 'Trap' in file:a=decompress_(a,ZSTD_DICT);file3=file;check_file3=True
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{decompress}/{file}','wb') as f1:
                            f1.write(a)
                thu=False
                try:
                    filexml='./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,file2)
                    byt=open(filexml, 'rb')
                    i=0
                    nod={}
                    ofs = getint()
                    stri = getstr()
                    if stri == 'Element':
                        stri1 = 'Item'
                    else:
                        stri1 = stri
                    byt.seek(4, 1)
                    aidx = getint()
                    ite = False
                    attr={}
                    for j in range(0, aidx):
                        attr1 = analyattr()
                        if type(attr1) == str:
                            text1 = attr1
                            ite = true
                        else:
                            attr.update(attr1)
                        root = ET.Element(stri1, attrib=attr)
                    if ite == True:
                        nod[myid].text = text1
                    checkfour()
                    chk = ofs - byt.tell()
                    if chk > 12:
                        byt.seek(4, 1)
                        sidx = getint()
                        for h in range(0, sidx):
                            analynode(None, byt.tell())
                    byt.close
                    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
                    xmlstr=mod_infos_mac_dinh(xmlstr,skinid.decode(),skin_phu_bac_a)
                    if veres_rt:
                        xmlstr=xmlstr.replace('Prefab_Hero/520_Veres/5208_Veres_LOD','Prefab_Hero/520_Veres/Component/5208_Veres_RT_'+str(int(skinid_veres[6:].decode())+1)+'_LOD')
                        xmlstr=xmlstr.replace('Prefab_Hero/520_Veres/5208_Veres_Show','Prefab_Hero/520_Veres/Component/5208_Veres_RT_'+str(int(skinid_veres[6:].decode())+1)+'_Show')
                        xmlstr=xmlstr.replace('_LOD1','_LOD2').replace('_LOD3','_LOD2')
                    else:
                        if HD_e:
                            xmlstr=xmlstr.replace('_LOD2','_LOD1').replace('_LOD3','_LOD1')
                            xmlstr=xmlstr.replace('_Show2','_Show1').replace('_Show3','_Show1')
                    if phu_kien and not veres_rt:
                        p=xmlstr.find('Prefab_Hero')
                        t=xmlstr[p:xmlstr.find('_LOD',p)+4]
                        print(t)
                        p2=t.find('/',12)
                        t2=t.replace(t[:p2],t[:p2]+'/Component').replace('_LOD',skinid_phu_kien[5:].decode()+'_LOD')
                        print(t[:-3]+'Show')
                        print(t[:p2]+'/Component')
                        xmlstr=xmlstr.replace(t,t2).replace(t[:-3]+'Show',t2[:-3]+'Show')
                    xmlstr=fix_ef_infos(xmlstr,decompress,skinid.decode())
                    if skinid in [b'18402',b'18404',b'18405',b'18406',b'18407',b'18408',b'53402',b'53405',b'54801',b'54802',b'54803',b'54804',b'53701',b'53702',b'11610',b'11611',b'53902',b'53903',b'53904',b'53502',b'53504',b'53510',b'53602',b'53605',b'53606',b'53608',b'53609']:
                        p=xmlstr.find('</bUnityLight>')
                        if p!=-1:
                            xmlstr=xmlstr.replace('True</bUnityLight>','False</bUnityLight>',1)
                    if skinid ==b'19015':
                        xmlstr=xmlstr.replace('\n   <useMecanim Var="String" Type="System.Boolean">True</useMecanim>','',1)
                    if skinid in [b'54402']:
                        xmlstr=xmlstr.replace('True</useTimeline>','False</useTimeline>',1).replace('\n   <TransConfigs Var="Array" Type="Assets.Scripts.GameLogic.TransformConfig[]">\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.TransformConfig"/>\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.TransformConfig"/>\n   </TransConfigs>\n   <LookAt Var="Com" Type="Assets.Scripts.GameLogic.CameraLookAt">\n      <Offset Var="Com" Type="UnityEngine.Vector3">\n         <x Var="String" Type="System.Single">-0.07700014</x>\n         <y Var="String" Type="System.Single">1.689991</y>\n         <z Var="String" Type="System.Single">-1.183998</z>\n      </Offset>\n      <Direction Var="Com" Type="UnityEngine.Vector3">\n         <x Var="String" Type="System.Single">0.144031</x>\n         <y Var="String" Type="System.Single">0</y>\n         <z Var="String" Type="System.Single">0.9895732</z>\n      </Direction>\n      <Duration Var="String" Type="System.Single">1</Duration>\n   </LookAt>\n   <LightConfig Var="Com" Type="Assets.Scripts.GameLogic.PrepareBattleLightConfig"/>\n   <IdleShowConfigs Var="Array" Type="Assets.Scripts.GameLogic.IdleShowConfig[]">\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.IdleShowConfig">\n         <DisableDirLight Var="String" Type="System.Boolean">True</DisableDirLight>\n      </Item>\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.IdleShowConfig">\n         <DisableDirLight Var="String" Type="System.Boolean">True</DisableDirLight>\n      </Item>\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.IdleShowConfig"/>\n   </IdleShowConfigs>','',1)
                    if skinid in [b'12912']:
                        xmlstr=xmlstr.replace('\n   <LobbyScale Var="String" Type="System.Single">1</LobbyScale>','\n   <useStateDrivenMecanim Var="String" Type="System.Boolean">True</useStateDrivenMecanim>',1)
                    with open(filexml, "w" , encoding="utf-8") as f:
                        f.write(xmlstr)
                    tree=ET.parse(filexml)
                    attr=b''
                    byt=bytenode(tree.getroot())
                    f=open(filexml,'wb')
                    f.write(byt)
                    f.close()
                except Exception as bug:
                    print('mod infos lỗi: ',bug)
                    thu=True;byt=''
                try:
                    if b'</Item>' in byt:thu=True
                except:
                    if '</Item>' in byt:thu=True
                if thu:
                    try:
                        with open(f'./Pmin_Sources/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{decompress}/{file2}','rb') as f:
                            strin=f.read()
                            strin=decompress_(strin,ZSTD_DICT)
                            skinid_infos=skinid[:3]+bytes(str(int(skinid[3:].decode())+1),'utf-8')
                            pos=strin.find(b'ElementE')
                            mac_dinh = strin[:pos-109]
                            skinprefabg2=skinprefabg = strin[pos-109:pos-8]
                            while pos!=-1:
                                skin=strin[pos-8:pos-8+hex_to_dec(strin[pos-8:pos-6])]
                                if b'/'+skinid_infos+b'_' in skin:
                                    break
                                pos=strin.find(b'ElementE',pos+hex_to_dec(strin[pos-8:pos-6])-8)
                            pos=mac_dinh.find(b'ArtPrefabLOD')
                            pos2=mac_dinh.find(b'LOD3',pos)
                            lod_mac_dinh=mac_dinh[pos-8:pos2+4]
                            pos = mac_dinh.find(b'ArtLobbyShowLOD')
                            pos2=mac_dinh.find(b'Show3',pos)
                            show_mac_dinh=mac_dinh[pos-8:pos2+5]
                            pos=skin.find(b'ArtSkinPrefabLOD')
                            pos2=skin.find(b'LOD3')
                            lod_skin=skin[pos-8:pos2+4].replace(b'ArtSkinPrefabLOD',b'ArtPrefabLOD')
                            lod_skin=dec_to_hex(hex_to_dec(lod_skin[:2])-4)+lod_skin[2:]
                            lod_skin=lod_skin[:4] + dec_to_hex(hex_to_dec(lod_skin[4:6])-4) + lod_skin[5:]
                            pos=skin.find(b'ArtSkinLobbyShowLOD')
                            pos2=skin.find(b'Show3',pos)
                            show_skin=skin[pos-8:pos2+5].replace(b'ArtSkinLobbyShow',b'ArtLobbyShow')
                            show_skin=dec_to_hex(hex_to_dec(show_skin[:2])-4)+show_skin[2:]
                            show_skin=show_skin[:4]+dec_to_hex(hex_to_dec(show_skin[4:6])-4) + show_skin[5:]
                            #strin=strin.replace(lod_mac_dinh,lod_skin).replace(show_mac_dinh,show_skin)
                            cam_skin_find=skin.find(b'ArtSkinLobbyShowCamera')
                            #useNewMecanim
                            if cam_skin_find!=-1:
                                cam_skin=skin[cam_skin_find-16:cam_skin_find+hex_to_dec(skin[cam_skin_find-8:cam_skin_find-6])-16]
                                use_find=skin.find(b'useNewMecanim')
                                if use_find!=-1:
                                    useNew = skin[use_find-16:use_find+73]
                                else:
                                    use_find=skin.find(b'ArtSkinLobbyShowMovie')
                                    if use_find!=-1:
                                        useNew=skin[use_find-16:use_find+hex_to_dec(skin[use_find-8:use_find-6])-16]
                                    else:
                                            useNew=b''
                                cam_mac_dinh_find=mac_dinh.find(b'ArtSkinLobbyShowCamera')
                                
                                if cam_mac_dinh_find!=-1:
                                    cam_mac_dinh=mac_dinh[cam_mac_dinh_find-16:cam_mac_dinh_find+hex_to_dec(mac_dinh[cam_mac_dinh_find-8:cam_mac_dinh_find-6])-16]
                                    strin=strin.replace(mac_dinh,mac_dinh.replace(lod_mac_dinh,lod_skin).replace(show_mac_dinh,show_skin).replace(cam_mac_dinh,cam_skin+useNew))
                                else:
                                    strin=strin.replace(mac_dinh,mac_dinh.replace(lod_mac_dinh,lod_skin).replace(show_mac_dinh,show_skin))
                            else:
                                strin=strin.replace(mac_dinh,mac_dinh.replace(lod_mac_dinh,lod_skin).replace(show_mac_dinh,show_skin))
                            with open('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,file2),'wb') as f1:
                                if skinid==b'54402':
                                    strin=strin.replace(b'useTimeline',b'use0000line')
                                f1.write(strin)
                    except Exception as bug:
                        pass
                try:
                    if check_file3:
                        filexml='./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,file3)
                        byt=open(filexml, 'rb')
                        i=0
                        nod={}
                        ofs = getint()
                        stri = getstr()
                        if stri == 'Element':
                            stri1 = 'Item'
                        else:
                            stri1 = stri
                        byt.seek(4, 1)
                        aidx = getint()
                        ite = False
                        attr={}
                        for j in range(0, aidx):
                            attr1 = analyattr()
                            if type(attr1) == str:
                                text1 = attr1
                                ite = true
                            else:
                                attr.update(attr1)
                            root = ET.Element(stri1, attrib=attr)
                        if ite == True:
                            nod[myid].text = text1
                        checkfour()
                        chk = ofs - byt.tell()
                        if chk > 12:
                            byt.seek(4, 1)
                            sidx = getint()
                            for h in range(0, sidx):
                                analynode(None, byt.tell())
                        byt.close
                        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
                        for i in range(10):
                            t=skinid[:3].decode()+'0'+str(i)
                            if xmlstr.find(t)!=-1:
                                xmlstr=xmlstr.replace(f'/{t}/','/')
                        xmlstr=mod_ef_sound2(xmlstr.encode('utf-8'),decompress,skinid).decode()
                        #xmlstr=xmlstr.replace
                        with open(filexml, "w" , encoding="utf-8") as f:
                            f.write(xmlstr)
                        tree=ET.parse(filexml)
                        attr=b''
                        byt=bytenode(tree.getroot())
                        f=open(filexml,'wb')
                        f.write(byt)
                        f.close()
                except Exception as bug:
                    print(bug)
                    pass
            #---------------------------All Sound--------------------------
                print('All Sound')
                if True:
                    id_0 = dec_to_hex(int(skinid[:3].decode()+'00'))
                    for nnn in range(1,30):
                        id_2 = dec_to_hex(int(skinid[:3].decode())*100+nnn)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/BattleBank.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x01\x00\x00\x00\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1 and id_2!=id_mod:
                                strin = strin.replace(b'\x01\x00\x00\x00\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x01\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/BattleBank.bytes','wb') as f1:
                                    f1.write(strin)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/ChatSound.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1 and id_2!=id_mod:
                                strin = strin.replace(b'\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/ChatSound.bytes','wb') as f:
                                    f.write(strin)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/HeroSound.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00'+id_0+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1 and id_2!=id_mod:
                                strin = strin.replace(b'\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/HeroSound.bytes','wb') as f:
                                    f.write(strin)  
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbyBank.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00\x00\x00\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1 and id_2!=id_mod:
                                strin = strin.replace(b'\x00\x00\x00\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbyBank.bytes','wb') as f1:
                                    f1.write(strin)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbySound.bytes','rb') as f:
                            strin = f.read()
                            pos = strin.find(b'\x00'+id_2 + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                            if pos!=-1 and id_2!=id_mod:
                                strin = strin.replace(b'\x00'+id_2+b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',b'\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Sound/LobbySound.bytes','wb') as f1:
                                    f1.write(strin)
            #-----------------------------------------------Mod HeroSkinShop------------------------------------------------------------#
                print('Mod HeroSkinShop')
                try:
                    
                    id_0 = dec_to_hex(int((skinid[:3]+b'00').decode()))
                    id_mod = dec_to_hex(int(skinid.decode()))
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','rb') as f:
                        strin = f.read()
                        hero_actor = hex(int(skinid[:3].decode()))[2:]
                        if len(hero_actor)%2 ==1:
                            hero_actor='0'+hero_actor
                        hero_actor=bytes.fromhex(hero_actor)
                        hero_actor = hero_actor[1:]+hero_actor[:1]
                        pos = strin.find(id_0+b'\x00\x00'+hero_actor)
                        if pos !=-1:
                            pos2 = strin[pos-4:pos-2]
                            pos2 = pos2.hex();pos2 = pos2[2:]+pos2[:2];pos2 = int(pos2,16)
                            hs_0 = strin[pos-4:pos+pos2]
                            pos = strin.find(id_mod+b'\x00\x00'+hero_actor)
                            if pos!=-1:
                                pos2 = hex_to_dec(strin[pos-4:pos-2])
                                hs_mod = strin[pos-4:pos+pos2]
                                if skinid==b'13311' or skinid==b'11620':
                                    with open(f'./Pmin_Sources/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','rb') as f:
                                        strin2 = decompress_(f.read(),ZSTD_DICT)
                                    pos = strin2.find(b'\x43\x41\x00\x00\xA7')
                                    hs_mod = strin2[pos-4:pos+hex_to_dec(strin2[pos-4:pos-2])]
                                    hs_mod=hs_mod.replace(b'\x43\x41\x00\x00\xA7',b'\xFF\x33\x00\x00\x85')
                                    hs_mod=hs_mod[:36]+b'\x0B'+hs_mod[37:]
                                    hs_mod=hs_mod.replace(b'Awake_Label_1',b'Awake_Label_5')
                                if skinid==b'16707':
                                    hs_mod=hs_mod.replace(b'Awake_Label_1',b'Awake_Label_5')

                        hs_mod = hs_mod[:4]+hs_0[4:][:2]+hs_mod[6:]
                        hs_mod = hs_mod[:36]+hs_0[36:][:1]+hs_mod[37:]
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','rb') as f:
                        strin = f.read()
                        strin = strin.replace(hs_0,hs_mod)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Shop/HeroSkinShop.bytes','wb') as f1:
                            f1.write(strin)
                except:
                    
                    print(Fore.RED+Style.BRIGHT+'Không Mod HeroSkinShop'+Style.RESET_ALL)
                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','rb') as f:
                    a=f.read()
                    if True:
                        if len(skin_phu_bac_a)>0:
                            skinid2=skin_phu_bac_a[0]
                            skinid2=int(skinid2[:3].decode())*100+int(skinid2[3:].decode())-1
                            skinid2=str(skinid2).encode('utf-8')
                        else:skinid2=skinid
                        skin=a.find(dec_to_hex(int(skinid2.decode()))+b'\x00\x00'+dec_to_hex(int(skinid2.decode()[:3])))
                        de=a.find(dec_to_hex(int(skinid2.decode()[:3]+'00'))+b'\x00\x00'+dec_to_hex(int(skinid2.decode()[:3])))
                        skin2=skin=a[skin-4:skin+hex_to_dec(a[skin-4:skin-2])]
                        de2=de=a[de-4:de+hex_to_dec(a[de-4:de-2])]
                        skin=skin[:36]+b'\x00'+skin[37:]
                        de=de[:36]+dec_to_hex(int(skinid2[3:].decode()))+de[37:]
                        a=a.replace(skin2,skin).replace(de2,de)
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/heroSkin.bytes','wb') as f:f.write(a)
            #-----------------------------------------------Mod Back------------------------------------------------------------#
                print('mod back')
                list_fix_lag_ef_back = []
                def split_code_back(a):
                    if True:
                        split_code=[]
                        p=a.find(b'    <Track trackName=')
                        while p!=-1:
                            code=a[p:a.find(b'    <Track trackName=',p+10)].replace(b'  </Action>\r\n</Project',b'')
                            split_code.append(code)
                            p=a.find(b'    <Track trackName=',p+10)
                    return split_code
                id_back = [b'10506', b'10506', b'10611', b'10611', b'10620', b'10620', b'10603', b'10603', b'10603', b'10714', b'10714', b'10705', b'10705', b'10809', b'10809', b'10801', b'10801', b'10801', b'10915', b'10915', b'10915', b'10915', b'10915', b'10915', b'10915', b'10915', b'11110', b'11110', b'11113', b'11113', b'11113', b'11115', b'11115', b'11119', b'11119', b'11120', b'11120', b'11105', b'11105', b'11107', b'11107', b'11107', b'11107', b'11212', b'11212', b'11202', b'11202', b'11202', b'11205', b'11205', b'11205', b'11611', b'11611', b'11611', b'11611', b'11611', b'11611', b'11611', b'11611', b'11611', b'11611', b'11614', b'11614', b'11614', b'11614', b'11614', b'11616', b'11616', b'11619', b'11619', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11604', b'11604', b'11607', b'11607', b'11607', b'11607', b'11607', b'11607', b'11808', b'11808', b'12008', b'12008', b'12304', b'12304', b'12606', b'12606', b'12608', b'12608', b'12812', b'12812', b'12801', b'12806', b'12806', b'12912', b'12912', b'12907', b'12907', b'13011', b'13011', b'13015', b'13015', b'13015', b'13015', b'13015', b'13005', b'13005', b'13005', b'13111', b'13112', b'13112', b'13112', b'13116', b'13116', b'13118', b'13118', b'13104', b'13104', b'13210', b'13210', b'13212', b'13212', b'13204', b'13204', b'13204', b'13311', b'13311', b'13313', b'13313', b'13609', b'13609', b'13612', b'13612', b'13613', b'13613', b'13705', b'13705', b'13706', b'13706', b'13706', b'13706', b'14109', b'14109', b'14109', b'14109', b'14109', b'14110', b'14110', b'14111', b'14111', b'14117', b'14117', b'14118', b'14118', b'14104', b'14104', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14213', b'14206', b'14206', b'14206', b'15009', b'15009', b'15009', b'15009', b'15012', b'15012', b'15013', b'15013', b'15015', b'15015', b'15015', b'15015', b'15004', b'15004', b'15007', b'15007', b'15007', b'15211', b'15211', b'15212', b'15212', b'15216', b'15216', b'15216', b'15202', b'15204', b'15204', b'15301', b'15301', b'15409', b'15409', b'15412', b'15412', b'15413', b'15413', b'15611', b'15611', b'15710', b'15710', b'15704', b'15704', b'15705', b'15705', b'15705', b'15705', b'16311', b'16311', b'16304', b'16304', b'16307', b'16307', b'16607', b'16607', b'16710', b'16711', b'16711', b'16711', b'16712', b'16712', b'16703', b'16703', b'16707', b'16707', b'16909', b'16909', b'17106', b'17106', b'17106', b'17106', b'17309', b'17309', b'18408', b'18408', b'18702', b'18702', b'19009', b'19009', b'19009', b'19009', b'19009', b'19009', b'19009', b'19009', b'19009', b'19012', b'19012', b'19013', b'19013', b'19015', b'19015', b'19002', b'19002', b'19007', b'19007', b'19007', b'19007', b'19109', b'19109', b'19509', b'19508', b'19508', b'19609', b'19609', b'19603', b'19603', b'19603', b'19603', b'19605', b'19605', b'19605', b'19605', b'20601', b'20601', b'50111', b'50111', b'50111', b'50112', b'50112', b'50117', b'50117', b'50119', b'50119', b'50105', b'50105', b'50105', b'50108', b'50108', b'50108', b'50604', b'50604', b'50604', b'50802', b'50802', b'51009', b'51009', b'51013', b'51013', b'51015', b'51015', b'51015', b'51015', b'51003', b'51003', b'51004', b'51004', b'51208', b'51305', b'51305', b'51306', b'51306', b'51504', b'51504', b'51802', b'51802', b'51802', b'51802', b'51802', b'51808', b'51808', b'52011', b'52011', b'52011', b'52011', b'52007', b'52007', b'52113', b'52113', b'52113', b'52108', b'52108', b'52204', b'52204', b'52414', b'52414', b'52414', b'52414', b'52404', b'52404', b'52407', b'52407', b'52710', b'52710', b'53107', b'53107', b'53309', b'53309', b'53304', b'53304', b'53308', b'53308', b'53308', b'53503', b'53503', b'53702', b'53702', b'53703', b'53703', b'54002', b'54002', b'54307', b'54307', b'54307', b'54307', b'54402', b'54402', b'54802', b'54802', b'54804', b'54804', b'54805', b'54805', b'56703', b'56703', b'56704', b'56704', b'59702', b'59702', b'59802', b'59802', b'59901', b'59901', b'13109']
                if skinid in id_back and may_yeu_mod:# ((check_bien_ve_ef or skinid in [b'15004',b'13311',b'16707',b'11620']) or ) and may_yeu_mod:
                    try:
                        name = b''
                        List=[]
                        List_ngoai_le=[b'eventType="GetHolidayResourcePathTick']
                        try:
                            with open(f'./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{skinid.decode()}_back.xml','rb') as f:
                                strin = f.read()
                                strin=decompress_(strin)
                                for code in split_code_back(strin):
                                    p=code.find(b'eventType="')
                                    p2=code.find(b'" guid="')
                                    if code[p:p2] == b'eventType="TriggerParticle':
                                        p_parent = code.find(b'parentResourceName')
                                        if p_parent!=-1:
                                            p2_parent = code.find(b'/>',p_parent)
                                            ef=code[p_parent:p2_parent].split(b'/')[-1].split(b'"')[0]
                                            ef=b'prefab_skill_effects/hero_skill_effects/'+hero_name+b'/'+skinid+b'/'+ef
                                            ef=b'        <String name="resourceName" value="'+ef+b'" refParamName="" useRefParam="false" />'
                                            lines = code.split(b'\r\n')
                                            for i, line in enumerate(lines):
                                                if b'resourceName' in line:
                                                    lines[i] = ef
                                                    break
                                            code = b'\r\n'.join(lines)
                                        else:
                                            continue
                                    if skinid[:3] in [b'537']:
                                        continue
                                    if skinid in [b'53702']:
                                        continue
                                    #if code[p:p2]==b'eventType="PlayAnimDuration' and skinid in [b'51504']:
                                    #    code = code.replace(b'<String name="clipName" value="',b'<String name="clipName" value="'+skinid+b'/')
                                    if code[p:p2] in List_ngoai_le:
                                        continue
                                    patterns = [
                                        rb'eventType\s*=\s*"PlayAnimDuration',
                                        rb'eventType\s*=\s*"SetObjectDirectionTick',
                                        rb'eventType\s*=\s*"ChangeHDHeightDuration',
                                        rb'eventType\s*=\s*"TriggerParticleTick',
                                    ]

                                    # Kiểm tra xem đoạn code[p:p2] có khớp bất kỳ mẫu nào không
                                    if any(re.search(pat, code[p:p2]) for pat in patterns):
                                        if b'enabled="true"' in code:
                                            p=code.find(b'<Condition')
                                            if p!=-1:
                                                p2=code.find(b'<Event eventName')
                                                code=code.replace(code[p:p2],b'')
                                            List.append(code)
                                #if skinid==b'15710':
                                #    name=name.replace(b'</Event>\r\n    </Track>\r\n    <Track trackName="GetResource[huijidi]" eventType="GetHolidayResourcePathTick" guid="f5fef0dc-285d-4e1d-8753-561e6bb56feb" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="GetHolidayResourcePathTick" time="0.000" isDuration="false" guid="a876e630-35af-4e8b-8e4a-d5e712532467">\r\n        <String name="holidayResourcePathPrefix" value="Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huijidi" refParamName="" useRefParam="false" />\r\n        <String name="outPathParamName" value="strReturnCityFall" refParamName="" useRefParam="false" />\r\n        <String name="outSoundEventParamName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="GetResource[huicheng]" eventType="GetHolidayResourcePathTick" guid="5b2bdf83-4771-4196-adea-1fd186427d17" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="GetHolidayResourcePathTick" time="0.000" isDuration="false" guid="a458373b-da86-47b6-a6bb-fede8ea3ea44">\r\n        <int name="battleEffectCfgID" value="11000" refParamName="" useRefParam="false" />\r\n        <String name="holidayResourcePathPrefix" value="Prefab_Skill_Effects/Inner_Game_Effect/returncity_holidays/Holiday0/huicheng_tongyong" refParamName="" useRefParam="false" />\r\n        <String name="outPathParamName" value="strReturnCityEffectPath" refParamName="" useRefParam="false" />\r\n        <String name="outSoundEventParamName" value="" refParamName="" useRefParam="false" />\r\n      ',b'').replace(b'\r\n    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="1b12d0e0-8e92-40e4-909a-72b21d52bcf5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="ef567983-128d-4105-a2f5-ecc614a244dc">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="clipName" value="Home" refParamName="" useRefParam="false" />\r\n        <int name="layer" value="3" refParamName="" useRefParam="false" />\r\n        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />\r\n        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />\r\n        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="c1f6bece-4d4f-4bb8-9f5b-ec448a721456" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="PlayAnimDuration" time="7.000" length="4.500" isDuration="true" guid="a4f9646e-2cf2-4952-9cde-8d892eead301">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="clipName" value="Gohome1" refParamName="" useRefParam="false" />\r\n        <int name="layer" value="3" refParamName="" useRefParam="false" />\r\n        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="94206a84-71ae-4795-8ecd-728b8df2f93e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="1037d202-d0de-4d35-b9d3-a4484a97c12e">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_02" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="" refParamName="strReturnCityEffectPath" useRefParam="true" />\r\n        <String name="bindPointName" value="Bone_Qiu" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bEnableOptCull" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlyFollowPos" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\r\n        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlySetAlpha" value="true" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>',b'\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="28dbc769-e471-407e-8108-9012ecf910d8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="6057cb60-5062-42e9-a6cd-09c8e9e7eb05">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_02" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/157_BuZhiHuoWu/15710/huicheng_tongyong_02" useRefParam="true" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>')
                        except:
                            pass
                        name=b''.join(List)
                        if skinid == b'15412':
                            name=b'''    <Track trackName="Pmin" eventType="CheckSkillCombineConditionTick" guid="216618f0-8c39-4789-903b-130507092006" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="37a8c180-8551-4dc1-870e-46049f6e392b">\r
        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="154999" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />
        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="Pmin" eventType="CheckSkillCombineConditionTick" guid="3965e0e3-dd4b-44b8-ba36-130507092006" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false" guid="bb954fcc-b78f-406a-bfb8-12c1bb2e3359">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="skillCombineId" value="254999" refParamName="" useRefParam="false" />
        <Enum name="checkOPType" value="5" refParamName="" useRefParam="false" />
        <int name="skillCombineLevel" value="1" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="ChangeHDHeightDuration3" eventType="ChangeHDHeightDuration" guid="3965e0e3-dd4b-44b8-ba36-682488d46550" enabled="false" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="ChangeHDHeightDuration" time="0.000" length="7.000" isDuration="true" guid="32824200-4e8e-4101-8d7d-be0ea0c313d1">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <int name="heightChange" value="700" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="216618f0-8c39-4789-903b-08ddecb68b45" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="PlayAnimDuration" time="0.000" length="7.000" isDuration="true" guid="96fa9d23-90bd-480b-af17-a12d8c342396">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Home2" refParamName="" useRefParam="false" />
        <int name="layer" value="3" refParamName="" useRefParam="false" />
        <bool name="bLoop" value="true" refParamName="" useRefParam="false" />
        <float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="PlayAnimDuration2" eventType="PlayAnimDuration" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="PlayAnimDuration" time="7.000" length="1.500" isDuration="true" guid="621e77cb-3dfc-40e3-8082-3e8603e3f7e2">
        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />
        <String name="clipName" value="Gohome2" refParamName="" useRefParam="false" />
        <int name="layer" value="3" refParamName="" useRefParam="false" />
        <bool name="alwaysAnimate" value="true" refParamName="" useRefParam="false" />
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="216618f0-8c39-4789-903b-130507092006" status="true" />
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">
        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01" refParamName="" useRefParam="true"/>
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>
     </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="216618f0-8c39-4789-903b-130507092006" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">
        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="3965e0e3-dd4b-44b8-ba36-130507092006" status="true" />
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">
        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01_r" refParamName="" useRefParam="true"/>
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>
     </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="3965e0e3-dd4b-44b8-ba36-130507092006" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">
        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01_r" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
    <Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="216618f0-8c39-4789-903b-130507092006" status="true" />
      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false">
        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huijidi_01" refParamName="" useRefParam="true"/>
        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false"/>
     </Event>
    </Track>
    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="201bd792-c933-43a0-a590-bec4367a2710" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Condition id="0" guid="216618f0-8c39-4789-903b-130507092006" status="true" />
      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true">
        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="objectSpaceId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/huicheng_tongyong_01" refParamName="" useRefParam="true"/>
        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false"/>
      </Event>
    </Track>
'''
                        if True:
                            if True:
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/back.xml','rb') as f:
                                    strin = f.read()
                                    if True:
                                        back_id = b'    <Track trackName="ReupCC_'+bytes(str(i),'utf-8')+b'" eventType="CheckHeroIdTick" guid="Mod_by_YOUTUBE_'+hero_name[:3]+b'" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="Mod_Vip">\r\n      <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n      <int name="heroId" value="'+hero_name[:3]+b'" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'
                                        goc_id = b'\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="3fcc5b3f-3a9c-495c-bddd-5e3b03e5c01b'
                                        condition_mod = b'<Condition id="Pmin" guid="Mod_by_YOUTUBE_'+hero_name[:3]+b'" status="true"/>'
                                        condition_mod_false = b'<Condition id="Pmin" guid="Mod_by_YOUTUBE_'+hero_name[:3]+b'" status="false"/>'
                                        name = name.replace(b'<Event eventName="',condition_mod+b'\r\n      <Event eventName="')
                                        ef=b'prefab_skill_effects/hero_skill_effects/'+hero_name+b'/'+skinid
                                        list_fix_lag_ef_back.append(ef.decode()+'/huijidi_01')
                                        list_fix_lag_ef_back.append(ef.decode()+'/huicheng_tongyong_01')
                                        list_fix_lag_ef_back.append(ef.decode()+'/jiasu_tongyong_01')
                                        #
                                        if stoptrack_code==b'':
                                            p_sua_track1=strin.find(b'    <Track trackName="GetResource[huijidi]"')
                                            p_sua_track2=strin.find(b'    <Track trackName="GetResource[huicheng]"')
                                            stoptrack_code=stoptrack_code+b'\r\n          <TrackObject id="'+str(strin[:p_sua_track1].count(b'<Track trackName=')).encode('utf-8')+b'" guid="Pmin_Vjp_Pro" />'+b'\r\n          <TrackObject id="'+str(strin[:p_sua_track2].count(b'<Track trackName=')).encode('utf-8')+b'" guid="Pmin_Vjp_Pro" />'
                                            p_sua_track_3=strin.find(b'    <Track trackName="TriggerParticle')
                                            while p_sua_track_3!=-1:
                                                stoptrack_code=stoptrack_code+b'\r\n          <TrackObject id="'+str(strin[:p_sua_track_3].count(b'<Track trackName=')).encode('utf-8')+b'" guid="Pmin_Vjp_Pro" />'
                                                p_sua_track_3=strin.find(b'    <Track trackName="TriggerParticle',p_sua_track_3+10)
                                        #xoa để đè all
                                        dem = 0
                                        split_code=split_code_back(strin[:strin.find(b'<Track trackName="Zalo_0357514770')])
                                        stoptrack_code_big = stoptrack_code
                                        ani_back = b''
                                        for code in split_code_back(strin[:strin.find(b'<Track trackName="Zalo_0357514770')]):
                                            code_goc=code
                                            check=b'</Event>\r\n      <SkinOrAvatarList id="ID_SKIN01" />\r\n      <SkinOrAvatarList id="ID_SKIN02" />\r\n      <SkinOrAvatarList id="ID_SKIN03" />\r\n      <SkinOrAvatarList id="ID_SKIN04" />\r\n      <SkinOrAvatarList id="ID_SKIN05" />\r\n      <SkinOrAvatarList id="ID_SKIN06" />\r\n      <SkinOrAvatarList id="ID_SKIN07" />\r\n      <SkinOrAvatarList id="ID_SKIN08" />\r\n      <SkinOrAvatarList id="ID_SKIN09" />\r\n      <SkinOrAvatarList id="ID_SKIN10" />\r\n      <SkinOrAvatarList id="ID_SKIN11" />\r\n      <SkinOrAvatarList id="ID_SKIN12" />\r\n      <SkinOrAvatarList id="ID_SKIN13" />\r\n      <SkinOrAvatarList id="ID_SKIN14" />\r\n      <SkinOrAvatarList id="ID_SKIN15" />\r\n      <SkinOrAvatarList id="ID_SKIN16" />\r\n      <SkinOrAvatarList id="ID_SKIN17" />\r\n      <SkinOrAvatarList id="ID_SKIN18" />\r\n      <SkinOrAvatarList id="ID_SKIN19" />\r\n      <SkinOrAvatarList id="ID_SKIN20" />\r\n      <SkinOrAvatarList id="ID_SKIN21" />\r\n      <SkinOrAvatarList id="ID_SKIN22" />\r\n      <SkinOrAvatarList id="ID_SKIN23" />\r\n      <SkinOrAvatarList id="ID_SKIN24" />\r\n      <SkinOrAvatarList id="ID_SKIN00" />'
                                            if b'GetHolidayResourcePathTick' in code:
                                                def add_filter_attribute(xml_bytes=code, IN=b'11'):
                                                    # Bước 1: Nếu có SkinAvatarFilterType thì thay giá trị
                                                    new_bytes, count = re.subn(
                                                        rb'(<Track[^>]*?)\sSkinAvatarFilterType="[^"]*"',
                                                        rb'\1 SkinAvatarFilterType="' + IN + rb'"',
                                                        xml_bytes
                                                    )

                                                    # Bước 2: Nếu không có thì thêm mới
                                                    if count == 0:
                                                        new_bytes = re.sub(
                                                            rb'(<Track[^>]*?)>',
                                                            rb'\1 SkinAvatarFilterType="' + IN + rb'">',
                                                            xml_bytes
                                                        )

                                                    return new_bytes
                                                code=add_filter_attribute()
                                                code=code.replace(b'</Event>',check.replace(b'ID_SKIN',skinid[:3]))
                                                strin=strin.replace(code_goc, code)
                                                dem+=1
                                            elif (b'resourceName' in code and b'SkinAvatarFilterType="11"' in code):
                                                code=code.replace(b'</Event>',check.replace(b'ID_SKIN',skinid[:3]))
                                                strin=strin.replace(code_goc, code)
                                                dem+=1
                                            elif b'<SkinOrAvatarList id="' + skinid in code:
                                                code=code.replace(b'</Event>',check.replace(b'ID_SKIN',skinid[:3]).replace(b'\r\n      <SkinOrAvatarList id="'+skinid+b'" />',b''))
                                                strin=strin.replace(code_goc, code)
                                        '''
                                        for i in range(len(split_code)):
                                            code_goc=code = split_code[i]
                                            if b'<SkinOrAvatarList id="' + skinid in code:
                                                if (b'clipName' in code or b'Animation' in code) and b'CheckAni' not in code:
                                                    ch_st = b'\r\n          <TrackObject id="'+str(i).encode('utf-8')+b'" guid="Pmin_Vjp_Pro" />'
                                                    if ch_st not in stoptrack_code_big:
                                                        stoptrack_code_big+=ch_st
                                                    if b'SkinAvatarFilterType="9"' in code:
                                                        p1=code.find(b'</Event>')+len('</Event>')
                                                        p2=code.find(b'\r\n    </Track>')
                                                        ani_back+=code.replace(b'SkinAvatarFilterType="9"', b'').replace(code[p1:p2],b'').replace(b'<Event eventName',condition_mod+b'\r\n      <Event eventName')'''
                                        #str(strin[:p_sua_track1].count(b'<Track trackName=')).encode('utf-8')+b'" guid="Pmin_Vjp_Pro" />\r\n          <TrackObject id="'+str(strin[:p_sua_track2].count(b'<Track trackName=')).encode('utf-8')+b'" guid="Pmin_Vjp_Pro" />\r\n        </Array>\r\n        <bool name="alsoStopNotStartedTrack" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
                                        back=back_id+b'    <Track trackName="Zalo_0357514770" eventType="TriggerParticleTick" guid="Zalo_0357514770" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      Pmin_Dep_Trai\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="Zalo_0357514770">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" useRefParam="false" />\r\n        <String name="resourceName" value="Pmin_Pro_Vip/huijidi_01" useRefParam="false" />\r\n        <float name="lifeTime" value="5.000" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" useRefParam="false" />\r\n        <bool name="bUseHeroLocalForward" value="true" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Zalo_0357514770" eventType="TriggerParticle" guid="Zalo_0357514770" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      Pmin_Dep_Trai\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="Zalo_0357514770">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" useRefParam="false" />\r\n        <String name="resourceName" value="Pmin_Pro_Vip/huicheng_tongyong_01" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" useRefParam="false" />\r\n        <bool name="bEnableOptCull" value="false" useRefParam="false" />\r\n        <bool name="bTrailProtect" value="true" useRefParam="false" />\r\n        <String name="syncAnimationName" useRefParam="false" />\r\n        <bool name="bApplySpecialEffect" value="true" useRefParam="false" />\r\n        <bool name="bOnlySetAlpha" value="true" useRefParam="false" />\r\n        <String name="customTagName" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'#    <Track trackName="Zalo_0357514770" eventType="StopTracks" guid="Zalo_0357514770" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      Pmin_Dep_Trai\r\n      <Event eventName="StopTracks" time="0.000" isDuration="false" guid="Zalo_0357514770">\r\n        <Array name="trackIds" useRefParam="false" type="TrackObject">'+stoptrack_code_big+b'\r\n        </Array>\r\n        <bool name="alsoStopNotStartedTrack" value="true" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'#+ani_back
                                        #back=back_id + b'    <Track trackName="Zalo_0357514770" eventType="TriggerParticleTick" guid="Zalo_0357514770" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      Pmin_Dep_Trai\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="Zalo_0357514770">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" useRefParam="false" />\r\n        <String name="resourceName" value="Pmin_Pro_Vip/huijidi_01" useRefParam="false" />\r\n        <float name="lifeTime" value="5.000" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" useRefParam="false" />\r\n        <bool name="bUseHeroLocalForward" value="true" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="Zalo_0357514770" eventType="TriggerParticle" guid="Zalo_0357514770" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      Pmin_Dep_Trai\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="Zalo_0357514770">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" useRefParam="false" />\r\n        <String name="resourceName" value="Pmin_Pro_Vip/huicheng_tongyong_01" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" useRefParam="false" />\r\n        <bool name="bEnableOptCull" value="false" useRefParam="false" />\r\n        <bool name="bTrailProtect" value="true" useRefParam="false" />\r\n        <String name="syncAnimationName" useRefParam="false" />\r\n        <bool name="bApplySpecialEffect" value="true" useRefParam="false" />\r\n        <bool name="bOnlySetAlpha" value="true" useRefParam="false" />\r\n        <String name="customTagName" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'
                                        back=back.replace(b'Pmin_Dep_Trai',condition_mod).replace(b'Pmin_Pro_Vip',ef)
                                        back_need_2=back_need_
                                        if skinid in [b'50604',b'15004',b'51504',b'13311',b'11620']:
                                            strin=strin.replace(b'<Event eventName="PlayAnimDuration"',condition_mod_false+b'\r\n      <Event eventName="PlayAnimDuration"',3)
                                            if skinid in [b'50604',b'15004',b'51504']:back_need_2=back_need_2.replace(b'clipName" value="',b'clipName" value="'+skinid+b'/')
                                            if skinid == b'13311':
                                                back_need_2=back_need_2.replace(b'clipName" value="',b'clipName" value="13311/Awaken/')
                                            if skinid == b'11620':
                                                back_need_2=back_need_2.replace(b'clipName" value="',b'clipName" value="11620/Awaken/')
                                        else:back_need_2=b''
                                        if skinid in [b'16707',b'13311',b'11620']:
                                            back=back.replace(b'/'+skinid+b'/',b'/')
                                            back=mod_ef_sound(back,decompress,skinid,file,folder_mod)
                                        if skinid==b'15412':
                                            name=name.replace(b'enabled="false',b'enabled="true')
                                            back=back.replace(b'prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huicheng_tongyong_01"',b'prefab_skill_effects/hero_skill_effects/154_HuaMuLan/PMIN/huicheng_tongyong_01"')
                                            back=back.replace(b'prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huijidi_01"',b'prefab_skill_effects/hero_skill_effects/154_HuaMuLan/PMIN/huijidi_01"')
                                            name=name+b'\r\n    <Track trackName="ReupCC_" eventType="TriggerParticle" guid="ca420146-9732-4190-9790-c214efc6e549" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="43" guid="c5b40dad-9d13-446a-b218-c0052003d0e9" status="true" />\r\n      <Condition id="29" guid="Mod_by_YOUTUBE_154" status="true"/>\r\n      <Event eventName="TriggerParticle" time="0.000" length="7.000" isDuration="true" guid="37743f3e-8508-41df-9c61-5b44988c3889">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huicheng_tongyong_01" useRefParam="true" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="-0.300" z="0.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bEnableOptCull" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bTrailProtect" value="true" refParamName="" useRefParam="false" />\r\n        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <bool name="bApplySpecialEffect" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="bOnlySetAlpha" value="true" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="ReupCC" eventType="TriggerParticleTick" guid="372cea2b-4677-4587-a037-9c13affdb97d" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="38" guid="c5b40dad-9d13-446a-b218-c0052003d0e9" status="true" />\r\n      <Condition id="29" guid="Mod_by_YOUTUBE_154" status="true"/>\r\n      <Event eventName="TriggerParticleTick" time="7.000" isDuration="false" guid="007b4fc2-b841-493b-a390-91fde34a7624">\r\n        <TemplateObject name="targetId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/154_HuaMuLan/15412/huijidi_01" refParamName="strReturnCityFall" useRefParam="false" />\r\n        <float name="lifeTime" value="5.000" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false" />\r\n        <Enum name="ReplacementUsage" value="1" refParamName="" useRefParam="false" />\r\n        <Enum name="ReplacementSubUsage" value="1" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
                                        if skinid==b'51015':
                                            back=back.replace(b'510_Liliana/51015',b'PMin_MOD_VJP')
                                            strin=strin.replace(b'<Track trackName="51015" eventType="CheckSkinIdTick" guid="e533267d-58d5-4ce6-a189-960807c66be0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckSkinIdTick" time="0.006" isDuration="false" guid="cb365e06-972d-4d62-bd93-3c032678710e">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="skinId" value="51015',b'<Track trackName="PMIN_SIU_CAP" eventType="CheckHeroIdTick" guid="e533267d-58d5-4ce6-a189-960807c66be0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.006" isDuration="false" guid="cb365e06-972d-4d62-bd93-3c032678710e">\r\n        <TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="510')
                                        strin = strin.replace(b'  </Action>',back+name+back_need_2.replace(b'<Event eventName="PlayAnimDuration"',condition_mod+b'\r\n      <Event eventName="PlayAnimDuration"')+b'  </Action>')
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Back.xml','wb') as f1:
                                            f1.write(strin)
                        zz+=1;i+=1;j+=1
                    except Exception as bug:
                        print(bug)
                        print(Fore.RED+Style.BRIGHT+'Không Mod Biến Về'+Style.RESET_ALL)
            #-----------------------------------------------Mod LiteBullet------------------------------------------------------------#
                print('Mod LiteBullet')
                if skinid==b'15009':
                    for file in ['BlueBuff.xml','RedBuff_Slow.xml']:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/PassiveResource/{file}','rb') as f:
                            a=f.read()
                            a=a.replace(b'CheckSkinIdVirtualTick',b'CheckHeroIdTick').replace(b'skinId" value="15009',b'heroId" value="150')
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/PassiveResource/{file}','wb') as f:
                            f.write(a)
                print('mod organ')
                if skinid in [b"50108",b"14111",b"11107",b"15009",b"13015"]:
                    def organSkin(IDCHECK,folder_mod=folder_mod):
                        ID = IDCHECK
                        organSkin_mod=f"File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Actor/organSkin.bytes"
                        file = open(organSkin_mod, "rb")
                        IDN = str(hex(int(ID)))
                        IDN = IDN[4:6] + IDN[2:4]
                        IDN = bytes.fromhex(IDN)
                        ALL_ID = []
                        MD = int(ID[0:3] + "00")
                        for IDNew in range(21):
                            ALL_ID.append(str(MD))
                            MD += 1
                        ALL_ID.remove(ID)
                        for x in range(20):
                            IDK = str(hex(int(ALL_ID[x])))
                            IDK = IDK[4:6] + IDK[2:4]
                            IDK = bytes.fromhex(IDK)
                            ALL_ID[x] = IDK
                        Begin = file.read(140)
                        Read = b"\x00"
                        All = []
                        while Read != b"":
                            Read = file.read(36)
                            if Read.find(IDN) != -1:
                                All.append(Read)
                            try:
                                Max = Read[4] + (Read[5]*256)
                                Max0 = str(hex(Max))
                                if len(Max0) == 4:
                                    Max0 = Max0[2:4] + "00"
                                if len(Max0) == 5:
                                    Max0 = Max0[3:5] + "0" + Max0[2]
                                if len(Max0) == 6:
                                    Max0 = Max0[4:6] + Max0[2:4]
                                Max0 = bytes.fromhex(Max0)
                            except:
                                None
                        file.close()
                        file = open(organSkin_mod, "ab+")
                        Read0 = file.read()
                        for i in range(len(ALL_ID)):
                            for j in range(len(All)):
                                CT = All[j]
                                if CT.find(IDN) != -1:
                                    CT = CT.replace(IDN,ALL_ID[i])
                                else:
                                    CT = CT.replace(ALL_ID[i-1],ALL_ID[i])
                                CTN = str(hex(Max0[0]+(Max0[1]*256)+1))
                                if len(CTN) == 4:
                                    CTN = CTN[2:4]
                                if len(CTN) == 5:
                                    CTN = CTN[3:5] + "0" + CTN[2]
                                if len(CTN) == 6:
                                    CTN = CTN[4:6] + CTN[2:4]
                                CTN = bytes.fromhex(CTN)
                                OZ = b" \x00\x00\x00"
                                if len(CTN) == 1:
                                    CT = CT.replace(OZ+CT[4:6],OZ+CTN+b"\x00",1)
                                if len(CTN) == 2:
                                    CT = CT.replace(OZ+CT[4:6],OZ+CTN,1)
                                All[j] = CT
                                XXX = file.write(CT)
                                Max0 = CT[4:6]
                        file.close()
                        file = open(organSkin_mod, "rb")
                        Read = file.read()
                        Read = Read.replace(Begin[12:14],Max0,1)
                        file.close()
                        file = open(organSkin_mod, "wb")
                        Z = file.write(Read)
                        file.close()
                    organSkin(skinid.decode())
    #------------------------mod ăn bùa nak----------------------
                if skinid==b'15013':
                    for file in ['BlueBuff_CD.xml']:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/PassiveResource/{file}','rb') as f:
                            a=f.read()
                            a=decompress_(a,ZSTD_DICT)
                            check=b'    <Track trackName="15013" eventType="CheckHeroIdTick" guid="PMIN_MOD" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false" guid="reupCC">\r\n        <TemplateObject name="targetId" id="1" objectName="target" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="heroId" value="150" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>'
                            a=a.replace(b'  </Action>',check)
                            a=a.replace(b'<Event eventName="CheckSkinIdTick',b'<Condition id="pmin" guid="PMIN_MOD" status="true" />\r\n      <Event eventName="CheckSkinIdTick')
                            a=fix_ef_pro_vip(a,skinid)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/PassiveResource/{file}','wb') as f:
                            f.write(fix_condition(a))
                    for file in ['Dead_Born.xml']:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','rb') as f:
                            a=f.read()
                            for code in split_code_(a):
                                if b'skinId" value="15013' in code:
                                    a=a.replace(code,code.replace(b'CheckSkinIdVirtualTick',b'CheckHeroIdTick').replace(b'skinId" value="15013',b'heroId" value="150'))
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/{file}','wb') as f:
                            f.write(a)
    #------------------------mod ăn bùa nak----------------------
                print('mod ăn bùa nak')
                def mod_lite(folder_mod,hero_name,skinid):
                    try:
                        
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Skill/liteBulletCfg.bytes','rb') as f:
                            strin = f.read()
                            k=0
                            if skinid==b'13311':strin=strin.replace(b' hero_skill_effects/133_direnjie',b' component_effects/13311/13311_5',7)
                            if b'\x2f'+hero_name[:4] in strin and skinid!=b'13311':
                                if skinid+b'\x2f' in strin:
                                    strin = strin
                                else:
                                    while k<11:
                                        if k<10:
                                            id_04=id_0 = skinid[:3]+b'0'+bytes(str(k),'utf-8');id_0=id_0.decode();id_0 = hex(int(id_0))[2:]
                                        else:
                                            id_04=id_0 = skinid[:3]+bytes(str(k),'utf-8');id_0=id_0.decode();id_0 = hex(int(id_0))[2:]
                                        if len(id_0)==3:
                                            id_0='0'+id_0
                                        id_0 = bytes.fromhex(id_0)
                                        id_0 = id_0[1:]+id_0[:1]
                                        pos = strin.find(id_0+b'\x00')
                                        if pos!=-1:
                                            posid = strin.find(hero_name[:4],pos)
                                            posid2 = strin.find(b'\x2f',posid)
                                            re_a = a = strin[pos-4:posid2+1]
                                            pos = a.find(b'\xE8\x03\xE8\x03\xE8\x03')
                                            if pos!=-1:
                                                id_a = a[pos+6:pos+7]
                                                id_a = id_a.hex()
                                                id_a= int(id_a,16)+6
                                                id_a = hex(id_a)[2:]
                                                id_a = bytes.fromhex(str(id_a))
                                                a = a.replace(b'\xE8\x03\xE8\x03\xE8\x03'+a[pos+6:pos+7],b'\xE8\x03\xE8\x03\xE8\x03'+id_a)
                                                a = a.replace(a,a+skinid+b'\x2f')
                                                dau = a[:1]
                                                dau = dau.hex();dau = int(dau,16)+6
                                                dau = hex(dau)[2:]
                                                dau = bytes.fromhex(dau)
                                                a=a.replace(a,dau+a[1:])
                                                strin = strin.replace(re_a,a)
                                        else:
                                            if k<10:
                                                id_04=id_0 = b'3'+skinid[:3]+b'0'+bytes(str(k),'utf-8');id_0=id_0.decode();id_0 = hex(int(id_0))[2:]
                                            else:
                                                id_04=id_0 = b'3'+skinid[:3]+bytes(str(k),'utf-8');id_0=id_0.decode();id_0 = hex(int(id_0))[2:]
                                            if len(id_0)==5:
                                                id_0 = '0'+id_0
                                            id_0 = bytes.fromhex(id_0)
                                            id_0 = id_0[2:]+id_0[1:][:1]+id_0[:1]
                                            pos = strin.find(id_0)
                                            if pos!=-1:
                                                posid = strin.find(hero_name[:4],pos)
                                                posid2 = strin.find(b'\x2f',posid)
                                                re_a = a = strin[pos-4:posid2+1]
                                                pos = a.find(b'\xE8\x03\xE8\x03\xE8\x03')
                                                if pos!=-1:
                                                    id_a = a[pos+6:pos+7]
                                                    id_a = id_a.hex()
                                                    id_a= int(id_a,16)+6
                                                    id_a = hex(id_a)[2:]
                                                    id_a = bytes.fromhex(str(id_a))
                                                    a = a.replace(b'\xE8\x03\xE8\x03\xE8\x03'+a[pos+6:pos+7],b'\xE8\x03\xE8\x03\xE8\x03'+id_a)
                                                    a = a.replace(a,a+skinid+b'\x2f')
                                                    dau = a[:1]
                                                    dau = dau.hex();dau = int(dau,16)+6
                                                    dau = hex(dau)[2:]
                                                    dau = bytes.fromhex(dau)
                                                    a=a.replace(a,dau+a[1:])
                                                    strin = strin.replace(re_a,a)
                                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Skill/liteBulletCfg.bytes','wb') as f1:
                                            f1.write(strin)
                                        k+=1
                    except:
                        print(Fore.RED+Style.BRIGHT+'Không Mod Đánh Thường'+Style.RESET_ALL)
                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Skill/liteBulletCfg.bytes','rb') as f:a=f.read()
                if b'/'+skinid[:3]+b'_' in a and hieu_ung==b'\x8f':
                    if skinid!=b'13311':
                        mod_lite(folder_mod,hero_name,skinid)
                    else:
                        a=a.replace(b'hero_skill_effects/133_direnjie/',b'component_effects/13311/13311_5/')
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Skill/liteBulletCfg.bytes','wb') as f:f.write(a)


                        #-mod aov-
                if skinid==b'13311':
                    inp = f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/'
                    for file in listdir(inp+f'Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill'):
                        with open(inp+f'Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','rb') as f:
                            strin=f.read()
                            strin=decompress_(strin)
                            pos=strin.find(b'<String name="eventName" value="')
                            while pos!=-1:
                                pos2=strin.find(b'" refParamName=""',pos)
                                sound_find=strin[pos:pos2]
                                if b'_Voice_' in sound_find and b'_aw' not in sound_find:
                                    strin=strin.replace(sound_find,sound_find+b'_skin11_aw3')
                                if b'_Voice_' not in sound_find and b'_aw' not in sound_find:
                                    strin=strin.replace(sound_find,sound_find+b'_skin11_aw2')
                                pos=strin.find(b'<String name="eventName" value="',pos2)
                            with open(inp+f'Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:
                                f1.write(strin)
                    for file in ['BattleBank.bytes','ChatSound.bytes','HeroSound.bytes','LobbyBank.bytes','LobbySound.bytes']:
                        with open(inp+f'Databin/Client/Sound/{file}','rb') as f:
                            strin=f.read()
                            strin=strin.replace(b'\x00\xf4\x33\x00\x00',b'\x00\xff\xff\x00\x00').replace(b'\x00\xa0\x4f\x14\x00',b'\x00\xf4\x33\x00\x00').replace(b'\x00\x9f\x4f\x14\x00',b'\x00\xf4\x33\x00\x00')
                            if file =='BattleBank.bytes':strin=strin.replace(b'\x00\x9e\x4f\x14\x00',b'\x00\xf4\x33\x00\x00')
                            with open(inp+f'Databin/Client/Sound/{file}','wb') as f1:
                                f1.write(strin)
                if skinid==b'11620':
                    inp = f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/'
                    for file in listdir(inp+f'Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill'):
                        with open(inp+f'Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','rb') as f:
                            strin=f.read()
                            strin=decompress_(strin)
                            pos=strin.find(b'<String name="eventName" value="')
                            while pos!=-1:
                                pos2=strin.find(b'" refParamName=""',pos)
                                sound_find=strin[pos:pos2]
                                if b'_aw' not in sound_find:
                                    strin=strin.replace(sound_find,sound_find+b'_skin20_aw5')
                                pos=strin.find(b'<String name="eventName" value="',pos2)
                            with open(inp+f'Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:
                                f1.write(strin)
                    for file in ['BattleBank.bytes','ChatSound.bytes','HeroSound.bytes','LobbyBank.bytes','LobbySound.bytes']:
                        with open(inp+f'Databin/Client/Sound/{file}','rb') as f:
                            strin=f.read()
                            strin=strin.replace(b'\x00\x50\x2d\x00\x00',b'\x00\xff\xff\x00\x00').replace(b'\x00\x15\xbb\x11\x00',b'\x00\x50\x2d\x00\x00').replace(b'\x00\x16\xbb\x11\x00',b'\x00\x50\x2d\x00\x00')
                            with open(inp+f'Databin/Client/Sound/{file}','wb') as f1:
                                f1.write(strin)
                if skinid==b'16707':
                    inp = f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/'
                    for file in listdir('./Pmin_Sources/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/skill/'.format(decompress)):
                        if '.xml' in file:
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','rb') as f:
                                strin = decompress_(f.read())
                                if 'y' in co_ma_nguon_khong or 'Y' in co_ma_nguon_khong:strin=strin[:-1];strin=decompress_(strin,ZSTD_DICT)
                                pos = strin.find(b'<Track trackName="PlayHeroSoundTick')
                                while pos!=-1:
                                    posid = strin.find(b'<String name="eventName" value="',pos)
                                    posid2 = strin.find(b'" refParamName',posid)
                                    sound = strin[posid:posid2]
                                    if b'_VO_' in sound:
                                        if b'_Skin7_Aw4' not in sound:
                                            strin = strin.replace(sound,sound+b'_Skin7_Aw4')
                                    else:
                                        if b'_Skin7_Aw3' not in sound:
                                            strin = strin.replace(sound,sound+b'_Skin7_Aw3')
                                    pos = strin.find(b'<Track trackName="PlayHeroSoundTick',posid2)
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/skill/{file}','wb') as f1:
                                    f1.write(strin)
                    for file in ['BattleBank.bytes','ChatSound.bytes','HeroSound.bytes','LobbyBank.bytes','LobbySound.bytes']:
                        with open(inp+f'Databin/Client/Sound/{file}','rb') as f:
                            strin=f.read()
                            strin=strin.replace(b'\x00\x3c\x41\x00\x00',b'\x00\xff\xff\x00\x00').replace(b'\x00\x30\x7e\x19\x00',b'\x00\x3c\x41\x00\x00').replace(b'\x00\x2f\x7e\x19\x00',b'\x00\x3c\x41\x00\x00')
                            with open(inp+f'Databin/Client/Sound/{file}','wb') as f1:
                                f1.write(strin)
                try:
                    if True:
                        if not os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/imprint'.format(folder_mod,decompress)):
                            DIR = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/skill'.format(folder_mod,decompress)
                            DIR2 = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/skill'.format(folder_mod,decompress)
                            nonee = './{}/skill'.format(decompress)
                            with zipfile.ZipFile('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/Actor_{}_Actions.pkg.bytes'.format(folder_mod,hero_name[:3].decode()), 'w', zipfile.ZIP_STORED) as zipf:
                                zipdir('tmp/', zipf)
                        else:
                            def zipdir4(path, ziph):
                                for ii in listdir(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{decompress}/'):
                                    nonee = f'./{decompress}/{ii}'
                                    DIR = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,ii)
                                    DIR2 = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}/{}'.format(folder_mod,decompress,ii)
                                    for root, dirs, files in os.walk(DIR):
                                        for file in listdir(DIR2):
                                            ziph.write(os.path.join(root, file),
                                                    os.path.relpath(os.path.join(nonee,file),
                                                                    os.path.join(path, '..')))
                            with zipfile.ZipFile('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/Actor_{}_Actions.pkg.bytes'.format(folder_mod,hero_name[:3].decode()), 'w', zipfile.ZIP_STORED) as zipf:
                                zipdir4('tmp/', zipf)
                        if skinid[:3]==b'526' or skinid[:3]==b'137':
                            os.mkdir(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{decompress}')
                            os.mkdir(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{decompress}_pet')
                            with open(f'./Pmin_Sources/Resources/1.58.1/Prefab_Characters/Prefab_Pet/{decompress}_Pet/{decompress}_Pet_actorinfo.bytes','rb') as f:a=f.read()
                            if skinid[:3]==b'526':
                                a=decompress_(a,ZSTD_DICT)
                                t=str(int(skinid[3:].decode())+1).encode('utf-8')
                                if len(t)==1:
                                    for i in range(1,10):
                                        if str(i).encode('utf-8')!=t:
                                            a=a.replace(skinid[:3]+str(i).encode('utf-8'),skinid[:3]+t)
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{decompress}_pet/{decompress}_Pet_actorinfo.bytes','wb') as f:f.write(a)
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{decompress}/{decompress}_actorinfo.bytes','rb') as f:
                                a=f.read()
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{decompress}/{decompress}_actorinfo.bytes','wb') as f:
                                    f.write(a)
                            def zipdir3(path, ziph):
                                for ii in [decompress,f'{decompress}_pet']:
                                    nonee = './{}'.format(ii)
                                    DIR2 = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{}'.format(folder_mod,ii)
                                    DIR = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{}'.format(folder_mod,ii)
                                    for root, dirs, files in os.walk(DIR):
                                        for file in listdir(DIR2):
                                            ziph.write(os.path.join(root, file),
                                                    os.path.relpath(os.path.join(nonee,file),
                                                                    os.path.join(path, '..')))
                            with zipfile.ZipFile('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Actor_{}_Infos.pkg.bytes'.format(folder_mod,decompress[:3]), 'w', zipfile.ZIP_STORED) as zipf:
                                zipdir3('tmp/', zipf)
                            for file in listdir(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/'):
                                if 'bytes' not in file:
                                    shutil.rmtree(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/{file}')
                        if skinid[:3]!=b'526' and skinid[:3]!=b'137':
                            DIR = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress)
                            DIR2 = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress)
                            nonee = './Prefab_Hero/{}'.format(decompress)
                            with zipfile.ZipFile('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Actor_{}_Infos.pkg.bytes'.format(folder_mod,hero_name[:3].decode()), 'w', zipfile.ZIP_STORED) as zipf:
                                zipdir('tmp/', zipf)
                        if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress))== 1 :
                            shutil.rmtree('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,decompress))
                        if skinid[:3]!=b'526' and skinid[:3]!=b'137':
                            if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero'.format(folder_mod))== 1 :
                                shutil.rmtree('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Prefab_Characters/Prefab_Hero'.format(folder_mod))
                except:pass
            #----------------------------------Mod Motion--------------------------------------------#
                print('Mod Motion')
                try:
                    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes','rb') as f:
                        strin=f.read()
                        ID=skinid.decode()
                        List=[]
                        for i in range(30):
                            List.append(dec_to_hex(int(ID[:3]+'0'*(2-len(str(i)))+str(i))))
                        if True:
                            main=strin[140:]
                            List_code=[]
                            while True:
                                id=main[:2]
                                if dec_to_hex(int(ID))+b'\x00\x00' in main[:hex_to_dec(id)+4]:
                                    List_code.append(main[:hex_to_dec(id)+4])
                                for i in List:
                                    if i +b'\x00\x00' in main[:hex_to_dec(id)+4] and i+b'\x00\x00'!=dec_to_hex(int(skinid))+b'\x00\x00':
                                        List_code.append(main[:hex_to_dec(id)+4])
                                    else:break
                                main=main[hex_to_dec(id)+4:]
                                if main==b'':
                                    break
                            code_special=[]
                            code_normal_1=[]
                            code_normal_2=[]
                            for code in List_code:
                                if code[:2] in [b'6\x00',b'S\x00']:
                                    code_special.append(code)
                                else:
                                    code_normal_1.append(code)
                            if code_special!=[]:
                                code=code_special[0]
                                idcode=b'\x00\x00'+code[21:25]
                                for code in code_normal_1:
                                    for id in List:
                                        p=code.find(id+b'\x00\x00')
                                        if p!=-1:
                                            code=code.replace(code[p:p+8],id+idcode,1)
                                    code_normal_2.append(code)
                            else:
                                for code in code_normal_1:
                                    p=code.find(dec_to_hex(int(ID))+b'\x00\x00')
                                    if p!=-1:
                                        idcode=code[p+2:p+8]
                                        for id in List:
                                            p=code.find(id+b'\x00\x00')
                                            if p!=-1:
                                                code=code.replace(code[p:p+8],id+idcode,1)
                                    else:
                                        pass
                                    code_normal_2.append(code)
                            for i in range(len(code_normal_1)):
                                if len(code_normal_1)==len(code_normal_2):
                                    strin=strin.replace(code_normal_1[i],code_normal_2[i],1)
                            if len(code_special)+len(code_normal_1)==0:
                                for id in List:
                                    strin=strin.replace(id+b'\x00\x00',b'00\x00\x00',1)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes','wb') as f:f.write(strin)
                except:
                    print('\033[1;33mKhong Mod Motion')
                if skinid in [b'54402']:
                    try:
                        with open('Prefab_Gear.pkg.bytes','rb') as f:
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear.pkg.bytes','wb') as f1:
                                f1.write(f.read())
                    except:
                        if os.path.isdir(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear')== 0 :
                            shutil.copytree(f'./Pmin_Sources/resources/1.58.1/ages/prefab_gear',f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear')
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear/Defense/1338E1.xml','rb') as f:
                            strin=f.read()
                            strin=decompress_(strin,ZSTD_DICT)
                            ef=b'   <Track trackName="hihi" eventType="CheckHeroIdTick" guid="Mod_by_PminMod'+hero_name[3:]+b'" enabled="true" refParamName="" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\r\n        <int name="heroId" value="'+skinid[:3]+b'" refParamName="" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="reupCC" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" lod="0">\r\n      <Condition id="Pmin" guid="Mod_by_PminMod'+hero_name[3:]+b'" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="2.000" isDuration="true" guid="reupCC">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/'+hero_name+b'/'+skinid+b'/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" refParamName="" useRefParam="false" />\r\n        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false" />\r\n        <String name="syncAnimationName" value="" refParamName="" useRefParam="false" />\r\n        <String name="customTagName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'
                            strin=strin.replace(b' </Action>',ef+b' </Action>')
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear/Defense/1338E1.xml','wb') as f:
                                f.write(fix_condition(strin))
                        #shutil.make_archive(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear','zip',f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear')
                        #os.rename(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear.zip',f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear.pkg.bytes')
                        #shutil.rmtree(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Gear')
                #----------------------------------Mod Haste--------------------------------------------#
                try:
                    id_haste = [b'10611', b'10611', b'10611', b'10620', b'10620', b'10620', b'10620', b'11113', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11620', b'11607', b'11607', b'11607', b'11607', b'11607', b'11607', b'11607', b'11607', b'12304', b'12606', b'12706', b'13011', b'13011', b'13015', b'13015', b'13015', b'13015', b'13116', b'13116', b'13210', b'13210', b'13210', b'13210', b'13613', b'13613', b'13613', b'13613', b'13613', b'13613', b'14111', b'14111', b'14111', b'14111', b'14108', b'15009', b'15009', b'15012', b'15012', b'15012', b'15412', b'15710', b'16307', b'16307', b'18906', b'19007', b'19007', b'19007', b'19007', b'50112', b'50112', b'50112', b'50112', b'50108', b'50108', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'51015', b'52011', b'52011', b'52011', b'52414', b'52414', b'52414', b'52406', b'53703', b'54307', b'54307', b'54307', b'54307', b'54307', b'54402']
                    if skinid in id_haste and may_yeu_mod:#find_back>2 and may_yeu_mod and check_bien_ve_ef:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1.xml','rb') as f:
                            strin = f.read()
                            ef = b'   <Track trackName="CheckHeroIdTick'+bytes(str(has),'utf-8')+b'" eventType="CheckHeroIdTick" guid="Mod_by_YOUTUBE'+hero_name[3:]+b'" enabled="true" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" useRefParam="false"/>\r\n        <int name="heroId" value="'+skinid[:3]+b'" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="IDSKIN_Mod_by_YOUTUBE" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="pmin" guid="Mod_by_YOUTUBE'+hero_name[3:]+b'" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="5.000" isDuration="true" guid="3f4a326c-6b74-4d7e-b9ac-f36378e06052">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" useRefParam="false" />\r\n        <uint name="RefLiteBulletID" value="0" useRefParam="false" />\r\n        <bool name="bChooseResourceNameByCamp" value="false" useRefParam="false" />\r\n        <String name="parentResourceName" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/'+hero_name+b'/'+skinid+b'/jiasu_tongyong_01" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" useRefParam="false" />\r\n      </Event>\r\n    </Track>' 
                            #ef = ef+b'\r\n    <Track trackName="StopTrack0" eventType="StopTrack" guid="6ede0c38-27a5-46b3-9517-35d37d24d0e8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="pmin" guid="Mod_by_YOUTUBE'+hero_name[3:]+b'" status="true" />\r\n      <Event eventName="StopTrack" time="0.000" isDuration="false" guid="a3dc6302-0432-4989-8285-33b9d8858480">\r\n        <TrackObject name="trackId" id="8" guid="412ea073-5944-46e4-ae5e-3037e855fda7" refParamName="" useRefParam="false" />\r\n        <bool name="alsoStopNotStartedTrack" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
                            ef=ef.replace(b'IDSKIN',skinid)
                            pos = strin.find(b'  </Action>')
                            if pos!=-1:
                                if skinid==b'15009':
                                    ef=ef.replace(skinid+b'/jiasu_tongyong_01" refParamName="" useRefParam="false"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600',skinid+b'/t2_spint" refParamName="" useRefParam="false"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000')
                                    ef=ef.replace(b'CheckHeroIdTick',b'CheckSkinIdTick').replace(b'heroId" value="'+skinid[:3],b'skinId" value="'+skinid[:3]+b'00')
                                if skinid==b'14111':
                                    ef=ef.replace(skinid+b'/jiasu_tongyong_01" refParamName="" useRefParam="false"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600',skinid+b'/14111_luoer_Sprint" refParamName="" useRefParam="false"/>\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000')
                                    ef=ef.replace(b'CheckHeroIdTick',b'CheckSkinIdTick').replace(b'heroId" value="'+skinid[:3],b'skinId" value="'+skinid[:3]+b'00')
                                if skinid==b'13210':
                                    ef=ef.replace(b'CheckHeroIdTick',b'CheckSkinIdTick').replace(b'heroId" value="'+skinid[:3],b'skinId" value="'+skinid[:3]+b'00')
                                strin = strin.replace(b' </Action>',ef+b'\n  </Action>')
                                with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1.xml','wb') as f1:
                                    f1.write(strin)
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1_leave.xml','rb') as f:
                            strin = f.read()
                            ef = b'   <Track trackName="CheckHeroIdTick'+bytes(str(has),'utf-8')+b'" eventType="CheckHeroIdTick" guid="Mod_by_YOUTUBE'+hero_name[3:]+b'" enabled="true" useRefParam="false" r="0.667" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="CheckHeroIdTick" time="0.000" isDuration="false">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" useRefParam="false"/>\r\n        <int name="heroId" value="'+skinid[:3]+b'" useRefParam="false"/>\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="IDSKIN_Mod_by_YOUTUBE" enabled="true" useRefParam="false" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="pmin" guid="Mod_by_YOUTUBE'+hero_name[3:]+b'" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="5.000" isDuration="true" guid="3f4a326c-6b74-4d7e-b9ac-f36378e06052">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" useRefParam="false" />\r\n        <uint name="RefLiteBulletID" value="0" useRefParam="false" />\r\n        <bool name="bChooseResourceNameByCamp" value="false" useRefParam="false" />\r\n        <String name="parentResourceName" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/'+hero_name+b'/'+skinid+b'/jiasu_tongyong_01" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
                            #ef=ef+b'\r\n    <Track trackName="StopTrack0" eventType="StopTrack" guid="6ede0c38-27a5-46b3-9517-35d37d24d0e8" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="69" guid="Mod_by_YOUTUBE'+hero_name[3:]+b'" status="true" />\r\n      <Event eventName="StopTrack" time="0.000" isDuration="false" guid="a3dc6302-0432-4989-8285-33b9d8858480">\r\n        <TrackObject name="trackId" id="8" guid="412ea073-5944-46e4-ae5e-3037e855fda7" refParamName="" useRefParam="false" />\r\n        <bool name="alsoStopNotStartedTrack" value="true" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>'
                            ef=ef.replace(b'IDSKIN',skinid)
                            if skinid==b'15009':
                                ef =ef.replace(skinid+b'/jiasu_tongyong_01',skinid+b'/t2_spint').replace(b'y="0.700" z="-0.600',b'y="0.000" z="0.000')
                                ef=ef.replace(b'CheckHeroIdTick',b'CheckSkinIdTick').replace(b'heroId" value="'+skinid[:3],b'skinId" value="'+skinid[:3]+b'00')
                            if skinid==b'14111':
                                ef =ef.replace(skinid+b'/jiasu_tongyong_01',skinid+b'/14111_luoer_Sprint').replace(b'0.000" y="0.700" z="-0.600',b'0.000" y="0.000" z="0.000')
                                ef=ef.replace(b'CheckHeroIdTick',b'CheckSkinIdTick').replace(b'heroId" value="'+skinid[:3],b'skinId" value="'+skinid[:3]+b'00')
                            if skinid==b'13210':
                                ef=ef.replace(b'CheckHeroIdTick',b'CheckSkinIdTick').replace(b'heroId" value="'+skinid[:3],b'skinId" value="'+skinid[:3]+b'00')
                            strin = strin.replace(b' </Action>',ef+b'\n  </Action>')
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1_leave.xml','wb') as f1:
                                f1.write(strin)
                except:
                    print(Fore.RED+Style.BRIGHT+'Không Mod Gia Tốc'+Style.RESET_ALL)
                #mod thông báo hạ gục
                try:
                    if skinid[:3] in [b'150']:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Huanhua/ResKillBillboardCfg.bytes','rb') as f:
                            killboard=f.read()
                            if skinid in [b'15015']:
                                killboard=killboard.replace(b'/18/',b'/20/')
                            elif skinid in [b'15012']:
                                killboard=killboard.replace(b'\x2C\x00\x00\x00\x10\x00\x00\x00\x1E\x00\x00\x00\x55\x49\x33\x44\x2F\x42\x61\x74\x74\x6C\x65\x2F\x42\x72\x6F\x61\x64\x63\x61\x73\x74\x2F\x31\x36\x2F\x7B\x30\x7D\x2F\x00\x01\x00\x00\x00\x00\x01',b'\x2B\x00\x00\x00\x10\x00\x00\x00\x1D\x00\x00\x00\x55\x49\x33\x44\x2F\x42\x61\x74\x74\x6C\x65\x2F\x42\x72\x6F\x61\x64\x63\x61\x73\x74\x2F\x39\x2F\x7B\x30\x7D\x2F\x00\x01\x00\x00\x00\x00\x01')
                            else:
                                killboard=killboard.replace(b'/18/',b'/16/')
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Huanhua/ResKillBillboardCfg.bytes','wb') as f:
                            f.write(killboard)
                except Exception as bug:
                    print(bug)
                #Mod assetrefs
                def indent(elem, level=0):
                    i = "\n" + "   " * level  # 3 space cho mỗi level thụt
                    if len(elem):
                        if not elem.text or not elem.text.strip():
                            elem.text = i + "   "  # Thêm space vào đầu nếu không có text
                        for e in elem:
                            indent(e, level + 1)
                        if not e.tail or not e.tail.strip():
                            e.tail = i
                    else:
                        if level and (not elem.tail or not elem.tail.strip()):
                            elem.tail = i

                # Hàm xử lý XML
                def move_and_insert_particles(xml_string: str, target_skin_id: str, v1_list: list[str]) -> str:
                    """
                    Kết hợp: chuyển particles từ skinSubset sang baseSubset nếu v1 khớp target_skin_id,
                    đồng thời thêm mới từ v1_list vào baseSubset.particlesInFirstLayer (mỗi cái v2=1, tự cộng nếu trùng).

                    Args:
                        xml_string (str): Nội dung XML.
                        target_skin_id (str): ID skin cần tìm trong skinSubset.
                        v1_list (list[str]): Danh sách item muốn thêm tay vào particlesInFirstLayer.

                    Returns:
                        str: XML đã xử lý.
                    """
                    from bs4 import BeautifulSoup
                    from collections import Counter

                    soup = BeautifulSoup(xml_string, "xml")
                    base_subset = soup.find("baseSubset")
                    skin_subset = soup.find("skinSubset")
                    if not base_subset:
                        return xml_string

                    def get_or_create_block(tag_name):
                        tag = base_subset.find(tag_name)
                        if not tag:
                            tag = soup.new_tag(tag_name)
                            tag.attrs = {
                                "Var": "Cus",
                                "Type": "System.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]"
                            }
                            base_subset.append(tag)
                        return tag

                    # ========== [PHẦN 1] DI CHUYỂN TỪ SKINSUBSET ==========
                    if skin_subset:
                        for item in skin_subset.find_all("Item", recursive=False):
                            v1_tag = item.find("v1")
                            if v1_tag and v1_tag.text.strip().lower() == target_skin_id.lower():
                                v2_tag = item.find("v2")
                                if not v2_tag:
                                    continue

                                for tag_name in ["particlesInFirstLayer", "hurtParticlesInFirstLayer"]:
                                    block = v2_tag.find(tag_name)
                                    if block:
                                        items = block.find_all("Item", recursive=False)
                                        target_block = get_or_create_block(tag_name)

                                        # map đã có
                                        existing_map = {
                                            i.find("v1").text.strip().lower(): i
                                            for i in target_block.find_all("Item", recursive=False)
                                            if i.find("v1") and i.find("v2")
                                        }

                                        for subitem in items:
                                            sub_v1 = subitem.find("v1").text.strip()
                                            sub_v2 = int(subitem.find("v2").text.strip())
                                            key = sub_v1.lower()

                                            if key in existing_map:
                                                old_v2_tag = existing_map[key].find("v2")
                                                old_v2 = int(old_v2_tag.text.strip())
                                                old_v2_tag.string = str(old_v2 + sub_v2)
                                            else:
                                                target_block.append(subitem)

                                        block.decompose()
                                break

                    # ========== [PHẦN 2] THÊM TAY TỪ DANH SÁCH ==========
                    if v1_list:
                        tag_name = "particlesInFirstLayer"
                        block = get_or_create_block(tag_name)
                        counter = Counter(v.strip().lower() for v in v1_list)

                        existing_map = {
                            item.find("v1").text.strip().lower(): item
                            for item in block.find_all("Item", recursive=False)
                            if item.find("v1") and item.find("v2")
                        }

                        for key, count in counter.items():
                            if key in existing_map:
                                old_v2_tag = existing_map[key].find("v2")
                                old_v2 = int(old_v2_tag.text.strip())
                                old_v2_tag.string = str(old_v2 + count)
                            else:
                                new_item = soup.new_tag("Item", attrs={
                                    "Type": "AssetRefAnalyser.Pair`2[System.String,System.Int32]",
                                    "Var": "Com"
                                })
                                new_v1 = soup.new_tag("v1", attrs={"Type": "System.String", "Var": "String"})
                                new_v1.string = key
                                new_v2 = soup.new_tag("v2", attrs={"Type": "System.Int32", "Var": "String"})
                                new_v2.string = str(count)
                                new_item.append(new_v1)
                                new_item.append(new_v2)
                                block.append(new_item)

                    return str(soup)


                def process_xml(data, v1_id=None):

                    data = data.strip()

                    # Parse XML
                    root = ET.fromstring(data)

                    # Tìm baseSubset
                    base_subset = root.find("baseSubset")
                    if base_subset is None:
                        base_subset = ET.SubElement(root, "baseSubset")

                    # Tạo dictionary để quản lý các nhóm trong baseSubset
                    base_groups = {}
                    for child in base_subset:
                        base_groups[child.tag] = child

                    # Danh sách v1 để tái sử dụng
                    v1_list = []

                    # Xử lý skinSubset
                    # Xử lý skinSubset
                    for skin_subset in root.findall("skinSubset"):
                        for item in skin_subset.findall("Item"):
                            v1 = item.find("v1")
                            v2 = item.find("v2")

                            if v1 is not None:
                                v1_list.append(v1.text.strip())

                            if v2 is None:
                                continue

                            move_tags = []
                            for child in v2:
                                tag_name = child.tag
                                if tag_name in ["actions", "skillCombines", "hurtParticlesInFirstLayer", "animations"]:
                                    # Nếu baseSubset đã có nhóm này thì thêm vào
                                    if tag_name not in base_groups:
                                        base_groups[tag_name] = ET.SubElement(base_subset, tag_name)
                                        base_groups[tag_name].set("Var", "Cus")
                                        base_groups[tag_name].set("Type", child.get("Type"))

                                    for subitem in child.findall("Item"):
                                        base_groups[tag_name].append(subitem)

                                    move_tags.append(child)

                            # Xóa các nhóm đã move
                            for tag in move_tags:
                                v2.remove(tag)


                    # Thụt dòng cho XML đẹp
                    indent(root)


                    #return modified_data, v1_list
                    return root
                try:
                    if True:   
                        fix_lag=0
                        file=f'{skinid[:3].decode()}_AssetRef.bytes'
                        with open(f'./Pmin_Sources/Resources/1.58.1/AssetRefs/Hero/{file}','rb') as f:
                            strin = f.read()
                            strin=decompress_(strin,ZSTD_DICT)
                            if os.path.isdir(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/AssetRefs/') ==0:
                                os.makedirs(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/AssetRefs/')
                                os.makedirs(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/AssetRefs/Hero/')
                            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/AssetRefs/Hero/{file}','wb') as f1:
                                f1.write(strin)
                        filexml=f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/AssetRefs/Hero/{file}'
                        byt=open(filexml, 'rb')
                        i=0
                        nod={}
                        ofs = getint()
                        stri = getstr()
                        if stri == 'Element':
                            stri1 = 'Item'
                        else:
                            stri1 = stri
                        byt.seek(4, 1)
                        aidx = getint()
                        ite = False
                        attr={}
                        for j in range(0, aidx):
                            attr1 = analyattr()
                            if type(attr1) == str:
                                text1 = attr1
                                ite = true
                            else:
                                attr.update(attr1)
                            root = ET.Element(stri1, attrib=attr)
                        if ite == True:
                            nod[myid].text = text1
                        checkfour()
                        chk = ofs - byt.tell()
                        if chk > 12:
                            byt.seek(4, 1)
                            sidx = getint()
                            for h in range(0, sidx):
                                analynode(None, byt.tell())
                        byt.close
                        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
                        if skinid == b'13210':
                            xml_code='''<Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">132111</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">132117</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">132118</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">132119</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>'''
                            xmlstr=xmlstr.replace('''<Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">132111</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>''',xml_code)
                        if skinid==b'52414':
                            xml_code='''<Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">524043</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">524995</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">524998</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">524997</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>
         <Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">524996</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>'''
                            xmlstr=xmlstr.replace('''<Item Var="Com" Type="AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]">
            <v1 Var="String" Type="System.UInt32">524043</v1>
            <v2 Var="String" Type="System.Int32">1</v2>
         </Item>''',xml_code)
                            if skinid==b'11620':
                                xmlstr = process_xml(xmlstr,skinid.decode())
                                xmlstr=xmlstr.replace('11620_3','11620_5')
                        xmlstr=move_and_insert_particles(xmlstr, skinid.decode(), []) #list_fix_lag_ef_back)
                        xmlstr=fix_ef(mod_ef_sound2(xmlstr.encode('utf-8'),decompress,skinid),skinid).decode()
                        with open(filexml, "w" , encoding="utf-8") as f:
                            f.write(xmlstr)
                        tree=ET.parse(filexml)
                        attr=b''
                        byt=bytenode(tree.getroot())
                        f=open(filexml,'wb')
                        f.write(compress_(byt))
                        f.close()
                except Exception as bug:
                    print(bug)
    print('kết cục')
    def zipdir2(path, ziph):
        for ii in back_folder:
            nonee = './{}'.format(ii)
            DIR2 = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            DIR = './File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,ii)
            for root, dirs, files in os.walk(DIR):
                for file in listdir(DIR2):
                    ziph.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(nonee,file),
                                            os.path.join(path, '..')))
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Back.xml','rb') as f1:strin=f1.read()
    strin=fix_condition(strin)
    strin=strin.replace(b'\t',b'    ').replace(b'</Track>  </Action>',b'</Track>\r\n  </Action>')
    #if veres_rt:
    #    strin=strin.replace(b'prefab_skill_effects/hero_skill_effects/520_Veres/52007/',b'prefab_skill_effects/component_effects/52007/'+skinid_veres+b'/')
    strin=strin.replace(b'prefab_skill_effects/hero_skill_effects/527_Sephera/52709/huicheng_tongyong_01',b'Prefab_Skill_Effects/Inner_Game_Effect/returncity/returncity_151_Lan')
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Back.xml','wb') as f1:
        strin=xoa_thua_thai(strin)
        f1.write(compress_(strin,ZSTD_DICT))
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1.xml','rb') as f1:strin=f1.read()
    if raz_15710_back and False:
        strin=strin.replace(b'  </Action>',b'    <Track trackName="TriggerParticle0" eventType="TriggerParticle" guid="412ea073-5944-46e4-ae5e-3037e855fda7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Condition id="Pmin" guid="Mod_by_YOUTUBE_BuZhiHuoWu" status="true" />\r\n      <Event eventName="TriggerParticle" time="0.000" length="5.000" isDuration="true" guid="3f4a326c-6b74-4d7e-b9ac-f36378e06052">\r\n        <TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bChooseResourceNameByCamp" value="false" refParamName="" useRefParam="false" />\r\n        <String name="parentResourceName" value="" refParamName="" useRefParam="false" />\r\n        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/157_BuZhiHuoWu/15710/jiasu_tongyong_02" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n'+b'  </Action>')
    def split_code_(a):
        if True:
            split_code=[]
            p=a.find(b'    <Track trackName=')
            while p!=-1:
                code=a[p:a.find(b'    <Track trackName=',p+10)].replace(b'  </Action>\r\n</Project',b'')
                split_code.append(code)
                p=a.find(b'    <Track trackName=',p+10)
            return split_code
    #if murad_13116:
    #    strin=strin.replace(b'hero_skill_effects/131_libai/LiBai',b'hero_skill_effects/131_libai/13116/LiBai')
    #    strin=strin.replace(b'<int name="skinId" value="13116" refParamName="" useRefParam="false" />',b'<int name="skinId" value="13116" refParamName="" useRefParam="false" />\r\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />')
    strin=fix_condition(strin)
    strin=strin.replace(b'14111/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600',b'14111/14111_luoer_Sprint" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000').replace(b'15009/jiasu_tongyong_01" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.700" z="-0.600',b'15009/t2_spint" refParamName="" useRefParam="false" />\r\n        <Vector3 name="bindPosOffset" x="0.000" y="0.000" z="0.000')
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1.xml','wb') as f1:
        strin=xoa_thua_thai(strin)
        f1.write(compress_(strin,ZSTD_DICT))
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1_leave.xml','rb') as f1:strin=f1.read()
    if False:
        strin=strin.replace(b'<Condition id="8" guid="b35fc6fe-6e4b-4c90-aded-6967f9755a4f" status="true" />',b'<Condition id="8" guid="b35fc6fe-6e4b-4c90-aded-6967f9755a4f" status="false" />')
        for a in strin.split(b'<Track trackName'):
            a2=a
            if b'b35fc6fe-6e4b-4c90-aded-6967f9755a4f" enabled="true' in a:
                a=a.replace(b'CheckSkinIdTick',b'CheckHeroIdTick').replace(b'skinId" value="15412',b'heroId" value="154')
                a=a.replace(b'\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'')
                strin=strin.replace(a2,a)
            if b'cc778ae2-88da-46de-b90f-1c3816a1065a" enabled="true' in a:
                a=a.replace(b'CheckSkinIdTick',b'CheckHeroIdTick').replace(b'skinId" value="15412',b'heroId" value="154')
                #a=a.replace(b'\r\n        <bool name="bEqual" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bSkipLogicCheck" value="true" refParamName="" useRefParam="false" />',b'')
                strin=strin.replace(a2,a)
    #if murad_13116:
    #    strin=strin.replace(b'hero_skill_effects/131_libai/LiBai',b'hero_skill_effects/131_libai/13116/LiBai')
    #    strin=strin.replace(b'<int name="skinId" value="13116" refParamName="" useRefParam="false" />',b'<int name="skinId" value="13116" refParamName="" useRefParam="false" />\r\n        <bool name="useNegateValue" value="true" refParamName="" useRefParam="false" />')
    strin=fix_condition(strin)
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/HasteE1_leave.xml','wb') as f1:
        strin=xoa_thua_thai(strin)
        f1.write(compress_(strin,ZSTD_DICT))
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Born.xml','rb') as f1:strin=f1.read()
    strin=fix_condition(strin)
    with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Born.xml','wb') as f1:
        strin=xoa_thua_thai(strin)
        f1.write(compress_(strin,ZSTD_DICT))
    with zipfile.ZipFile('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes'.format(folder_mod), 'w', zipfile.ZIP_STORED) as zipf:
        zipdir2('tmp/', zipf)
    ten_de_vao_ten=ten_de_vao_ten.encode('utf-8')
    with open(f'File_Mod/{folder_mod}/list.txt','wb') as f:f.write(ten_de_vao_ten)

    ten_de_vao_skill_an=ten_de_vao_skill_an.encode('utf-8')
    with open(f'File_Mod/{folder_mod}/skill_an(checkskinidtick).txt','wb') as f:f.write(ten_de_vao_skill_an)
    for iii in back_folder:
        if os.path.isdir('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))== 1 :
            shutil.rmtree('./File_Mod/{}/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{}'.format(folder_mod,iii))
    #---------mod ResCharacterComponent.bytes-----
    try:
        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Character/ResCharacterComponent.bytes','rb') as f:
            a=f.read()
            p2=a[:14]
            p3=a[:12]+b'\x00\x00'
            a=a.replace(p2,p3,1)
            with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/Databin/Client/Character/ResCharacterComponent.bytes','wb') as f:f.write(compress_(a,ZSTD_DICT))
    except:
        print('\033[1;33mKhong Mod ResCharacterComponent.bytes')
    try:
        try:
            nut_bam=sys.argv[2]
        except:
            nut_bam=''
        if len(nut_bam)==5:
            for file in listdir('NutBam'):
                if nut_bam in file:
                    with open(f'Nutbam/{file}','rb') as f:
                        with open(f'./File_Mod/{folder_mod}/com.garena.game.kgvn/files/Resources/1.58.1/assetbundle/uisystem/atlas/primary/allshared.assetbundle','wb') as f2:
                            f2.write(f.read())
                    break
    except Exception as bug:
        pass
    print(Fore.GREEN+Style.BRIGHT+'--------------------- ĐÃ MOD XONG ----------------------')
    if cam_xa_goc!=100:
        print(Fore.GREEN+Style.BRIGHT+'--------------------- ĐANG MOD CAM XA ----------------------')
        if os.path.isdir(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%') == 0 :
            os.mkdir(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%')
        shutil.copytree(f'./File_Mod/{folder_mod}/com.garena.game.kgvn',f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn')
        try:
            giai_nen(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/','Actor_530_Actions.pkg.bytes')
        except:
            shutil.copytree(f'./Pmin_Sources/resources/1.58.1/ages/Prefab_Characters/Prefab_Hero/530_Dirak',f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak')
        hittringer_dirak=b'    <Track trackName="HitTriggerTick0" eventType="HitTriggerTick" guid="CAM_XA_PMIN_MOD" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="HitTriggerTick" time="0.000" isDuration="false" guid="REUP_CC">\r\n        <TemplateObject name="targetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="hitTargetId" id="0" objectName="self" isTemp="false" refParamName="" useRefParam="false" />\r\n        <int name="SelfSkillCombineID_1" value="530510" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="triggerId" id="-1" objectName="None" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>'
        cam_xa=b'    <Track trackName="SetCameraHeightDuration0" eventType="SetCameraHeightDuration" guid="PMIN_MOD" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SetCameraHeightDuration" time="0.000" length="1.000" isDuration="true" guid="REUP_CC">\r\n        <int name="slerpTick" value="0" refParamName="" useRefParam="false" />\r\n        <float name="heightRate" value="'+str(int(cam_xa_goc)/100).encode('utf-8')+b'" refParamName="" useRefParam="false" />\r\n        <bool name="bOverride" value="true" refParamName="" useRefParam="false" />\r\n        <bool name="leftTimeSlerpBack" value="true" refParamName="" useRefParam="false" />\r\n        <String name="refParamName" value="" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n  </Action>\r\n</Project>'
        giai_nen(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/','CommonActions.pkg.bytes')
        with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak/skill/P2E1.xml','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            p=a.find(b'<Track trackName="')
            a=a[:p]+cam_xa
            with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak/skill/P2E1.xml','wb') as f:f.write(compress_(a,ZSTD_DICT))
        with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/back.xml','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            a=a.replace(b'</Action>',hittringer_dirak)
            with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/back.xml','wb') as f:f.write(compress_(a,ZSTD_DICT))
        with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            a=a.replace(b'</Action>',hittringer_dirak)
            with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/born.xml','wb') as f:f.write(compress_(a,ZSTD_DICT))
        with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Heal5v5.xml','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            a=a.replace(b'</Action>',hittringer_dirak)
            with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Heal5v5.xml','wb') as f:f.write(compress_(a,ZSTD_DICT))
        with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Heal3v3.xml','rb') as f:
            a=f.read()
            a=decompress_(a,ZSTD_DICT)
            a=a.replace(b'</Action>',hittringer_dirak)
            with open(f'File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/commonresource/Heal3v3.xml','wb') as f:f.write(compress_(a,ZSTD_DICT))
        DIR = f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak/skill'
        DIR2 = f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak/skill'
        nonee = './530_Dirak/skill'
        with zipfile.ZipFile(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/Actor_530_Actions.pkg.bytes', 'w', zipfile.ZIP_STORED) as zipf:
            zipdir('tmp/', zipf)
        def zipdir_camxa(path, ziph):
            for ii in back_folder:
                nonee = './{}'.format(ii)
                DIR2 = f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{ii}'
                DIR = f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{ii}'
                for root, dirs, files in os.walk(DIR):
                    for file in listdir(DIR2):
                        ziph.write(os.path.join(root, file),
                                os.path.relpath(os.path.join(nonee,file),
                                                os.path.join(path, '..')))
        with zipfile.ZipFile(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/CommonActions.pkg.bytes', 'w', zipfile.ZIP_STORED) as zipf:
            zipdir_camxa('tmp/', zipf)
        if os.path.isdir(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak')== 1 :
            shutil.rmtree(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/530_Dirak')
        for iii in back_folder:
            if os.path.isdir(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{iii}')== 1 :
                shutil.rmtree(f'./File_Mod/{folder_mod}/CAM XA {cam_xa_goc}%/com.garena.game.kgvn/files/Resources/1.58.1/Ages/Prefab_Characters/Prefab_Hero/{iii}')
    if nut_bam_auto_mod!='':
        nut = ''.join(re.findall(r'\d+', nut_bam_auto_mod))
        try:
            for inp in listdir('./Pmin_Sources/Resources'):
                break
            with open(f'NutBam/{nut}.Assetbundle','rb') as f:
                if os.path.isdir(f'./File_Mod/{folder_mod}/Nut Bam') == 0 :
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/{inp}/')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/{inp}/assetbundle/')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/{inp}/assetbundle/uisystem/')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/{inp}/assetbundle/uisystem/atlas')
                    os.mkdir(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/{inp}/assetbundle/uisystem/atlas/primary')
                with open(f'./File_Mod/{folder_mod}/Nut Bam/com.garena.game.kgvn/files/Resources/{inp}/assetbundle/uisystem/atlas/primary/ALLSHARED.ASSETBUNDLE','wb') as f1:f1.write(f.read())
        except Exception as Bug:
            print(Bug)
            print('Nút Bấm Không Tồn Tại')