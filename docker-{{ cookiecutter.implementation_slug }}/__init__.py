def get_supported_tls(version):
    """Return a list of all TLS versions supported by the specified version."""
    # Default to returning the versions supported by tlsprint
    return ["TLS10", "TLS11", "TLS12"]


def extract_versions(tags):
    """From a list of tags, extract the actual version numbers and add info
    about supported TLS versions.
    """
    # Default to use the tags as versions. For some implementations this is
    # sufficient, but for some additional stripping and filtering is needed.
    version_info = [{
        "tag": tag,
        "version": tag,
    } for tag in tags]

    # Add info about supported TLS versions
    for info in version_info:
        info["supported_tls"] = get_supported_tls(info["version"])

    return version_info
