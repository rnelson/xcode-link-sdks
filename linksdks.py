#!/usr/bin/env python
# 
# linksdks.py: script to symlink old platform SDKs into the current
#              version of Xcode (in /Applications/Xcode.app).
# 
# (c) 2014 Ross Nelson. Licensed under the zlib license.
# 
# rnelson@boxer /Developer $ ./linksdks.py
# Linked iPhoneOS7.1.sdk from Xcode 5.1.1 (iPhoneOS.platform)
# Linked MacOSX10.8.sdk from Xcode 5.1.1 (MacOSX.platform)
# Linked iPhoneOS6.1.sdk from Xcode 4.6.3 (iPhoneOS.platform)
# Linked iPhoneSimulator6.1.sdk from Xcode 4.6.3 (iPhoneSimulator.platform)
# Linked MacOSX10.7.sdk from Xcode 4.6.3 (MacOSX.platform)
# rnelson@boxer /Developer $
# 



from os import listdir, mkdir, symlink
from os.path import exists, isdir, islink, join

XCODEROOT = '/Developer/Xcode'
MYSDKROOT = '/Developer/SDKs'
APPSDKROOT = '/Applications/Xcode.app/Contents/Developer/Platforms'  # '/Developer/_test'
PLATFORMS = [d for d in listdir(APPSDKROOT) if d.endswith('.platform')]


def my_mkdir(path):
    if not exists(path):
        mkdir(path)


def ensure_platform_dirs():
    for p in PLATFORMS:
        platform_dir = join(APPSDKROOT, p)
        developer_dir = join(platform_dir, 'Developer')
        sdks_dir = join(developer_dir, 'SDKs')
        
        my_mkdir(platform_dir)
        my_mkdir(developer_dir)
        my_mkdir(sdks_dir)


def get_available_xcodes():
    # Get all folders matching the form 'Xcode <VERSION>.app'
    versions = [x for x in listdir(XCODEROOT) if isdir(join(XCODEROOT, x)) and x.startswith('Xcode ') and x.endswith('.app')]
    
    # Append those version numbers to our list and return it
    result = []
    [result.append(v[6:-4]) for v in versions]
    return reversed(sorted(result))


def main():
    ensure_platform_dirs()
    xcodes = get_available_xcodes()
    
    for version in xcodes:
        xcode_dir = join(XCODEROOT, 'Xcode {0}.app'.format(version))
        xcp_dir = join(xcode_dir, 'Contents/Developer/Platforms')
        
        for platform in PLATFORMS:
            platform_dir = join(xcp_dir, platform)
            
            if exists(platform_dir):
                sdks_dir = join(platform_dir, 'Developer/SDKs')
                sdks = [d for d in listdir(sdks_dir) if isdir(sdks_dir) and d.endswith('.sdk') and not islink(join(sdks_dir, d))]
                
                for sdk in sdks:
                    source = join(sdks_dir, sdk)
                    destination = join(join(APPSDKROOT, platform), 'Developer/SDKs/' + sdk)
                    versioned = sdk[-5:-4].isdigit()
                    
                    if versioned and not exists(destination):
                        symlink(source, destination)
                        print 'Linked ' + sdk + ' from Xcode ' + version + ' (' + platform + ')'


if __name__ == '__main__':
    main()
