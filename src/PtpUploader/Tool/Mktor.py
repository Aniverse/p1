from ..PtpUploaderException import PtpUploaderException
from ..Settings import Settings

from pyrocore.util import metafile

import os

def Make(logger, path, torrentPath):
    def Callback(meta):
        metafile.assign_fields( meta, [ 'info.source=PTP' ] )
    
    logger.info( "Making torrent from '%s' to '%s'." % ( path, torrentPath ) )
    torrent = metafile.Metafile(metapath)
    
    if os.path.exists( torrentPath ):
	raise PtpUploaderException( "Can't create torrent because path '%s' already exists." % torrentPath )
    
    torrent.create(datapath, Settings.PtpAnnounceUrl, created_by="PtpUploader", private=True, progress=None, callback=Callback)
        
