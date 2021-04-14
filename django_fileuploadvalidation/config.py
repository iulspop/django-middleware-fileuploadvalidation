from .data import whitelists

"""
    DETECTOR_SENSITIVITY
    Threshold from which the detector module denotes file as malicious.
    The higher the sensitivity the more strict the detector module.
"""
DETECTOR_SENSITIVITY = 0.98


"""
    UPLOAD_MIME_TYPE_WHITELIST
    Select the upload whitelist.
    This will only allow certain MIME types to be uploaded.

    Possible whitelists
    -------------------
    - whitelists.WHITELIST_MIME_TYPES__AUDIO_ALL
    - whitelists.WHITELIST_MIME_TYPES__APPLICATION_ALL
    - whitelists.WHITELIST_MIME_TYPES__IMAGE_ALL
    - whitelists.WHITELIST_MIME_TYPES__TEXT_ALL
    - whitelists.WHITELIST_MIME_TYPES__VIDEO_ALL

    - whitelists.WHITELIST_MIME_TYPES__AUDIO_RESTRICTIVE
    - whitelists.WHITELIST_MIME_TYPES__APPLICATION_RESTRICTIVE
    - whitelists.WHITELIST_MIME_TYPES__IMAGE_RESTRICTIVE
    - whitelists.WHITELIST_MIME_TYPES__TEXT_RESTRICTIVE
    - whitelists.WHITELIST_MIME_TYPES__VIDEO_RESTRICTIVE

    - whitelists.WHITELIST_MIME_TYPES__ALL
    - whitelists.WHITELIST_MIME_TYPES__RESTRICTIVE
"""
UPLOAD_MIME_TYPE_WHITELIST = whitelists.WHITELIST_MIME_TYPES__RESTRICTIVE

"""
    ALWAYS_ENABLED_UPLOADLOGS
    Set True, if the ReportBuilder module must log every upload attempt.
    Set False, if the ReportBuilder module should log successfull uploads. 
"""
ALWAYS_ENABLED_UPLOADLOGS = False