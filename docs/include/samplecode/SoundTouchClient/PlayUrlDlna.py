from bosesoundtouchapi import *
from bosesoundtouchapi.models import *
from bosesoundtouchapi.uri import *

try:
    
    # create SoundTouch device instance.
    device:SoundTouchDevice = SoundTouchDevice("192.168.1.81") # Bose SoundTouch 10
            
    # create SoundTouch client instance from device.
    client:SoundTouchClient = SoundTouchClient(device)

    # get current nowPlaying status.
    nowPlaying:NowPlayingStatus = client.GetNowPlayingStatus(True)
    print("\n(before): %s" % (nowPlaying.ToString()))

    # play the given url via the SoundTouch DLNA web server.
    print("\nPlaying URL content (http) via DLNA ...")
    client.PlayUrlDlna("http://edge-bauerall-01-gos2.sharp-stream.com/ghr70s.aac", 
                       "Greatest Hits Radio",
                       "70's Classic Hits",
                       "ghr70s.aac",
                       "https://image-cdn-ak.spotifycdn.com/image/ab67706c0000da849d37dd221d8aa1b35c545057")

    # get current nowPlaying status.
    nowPlaying:NowPlayingStatus = client.GetNowPlayingStatus(True)
    # do we have a source-specific nowplaying status?  if so, then return it.
    cacheKey = "%s-%s:%s" % (SoundTouchNodes.nowPlaying.Path, nowPlaying.Source, nowPlaying.SourceAccount)
    if cacheKey in client.ConfigurationCache:
        nowPlaying = client.ConfigurationCache[cacheKey]
    print("\n(after):  %s" % (nowPlaying.ToString()))
        
except Exception as ex:

    print("** Exception: %s" % str(ex))
