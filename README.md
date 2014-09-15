xcode-link-sdks
===============

About
-----

After upgrading to Xcode 6 GM and deleting Xcode 5.1.1, I notice that some 
[RubyMotion](http://rubymotion.com) code I have was not starting up correctly 
in the iOS 8 simulator.

RubyMotion allows you to force a specific SDK version and deployment target 
to use, so I set those both to 7.1:

```
app.sdk_version = '7.1'
app.deployment_target = '7.1'
```

The problem with this is that the 7.1 SDK doesn't ship with Xcode 6. I installed 
the 7.0 and 7.1 simulators, but still didn't have the SDK. I searched and found 
that the solution most people suggest is to simply download an old copy of Xcode 
and copy the SDKs into the appropriate path of the new version. With 6.1 already 
in beta, I wanted to automate the process for future Xcode releases.


Usage
-----

1. Create `/Developer` if it doesn't exist on your system; this is the directory 
   that Xcode used to live in, prior to being moved to a single large bundle in
   `/Applications`
2. Create an `Xcode` folder in `/Developer`
3. Download and copy any Xcode versions you want into that folder. Rename them to 
   `Xcode <VERSION>.app` (you may not see the `.app` in Finder)
4. Run `linksdks.py`

```
rnelson@boxer /Developer $ ./linksdks.py
Linked iPhoneOS7.1.sdk from Xcode 5.1.1 (iPhoneOS.platform)
Linked MacOSX10.8.sdk from Xcode 5.1.1 (MacOSX.platform)
Linked iPhoneOS6.1.sdk from Xcode 4.6.3 (iPhoneOS.platform)
Linked iPhoneSimulator6.1.sdk from Xcode 4.6.3 (iPhoneSimulator.platform)
Linked MacOSX10.7.sdk from Xcode 4.6.3 (MacOSX.platform)
rnelson@boxer /Developer $
```


Tips
----

If you have Gatekeeper installed, the first launching of a beta version of Xcode 
may take forever as the system verifies the checksums on 5 GB worth of files. If 
you use this script and future betas, you can mark an app bundle as safe with 
the following:

`xattr -d com.apple.quarantine /Applications/Xcode 6.1b1.app`


Caution
-------

This is simply the solution I found online for my problem. I assume this won't 
cause any problems, but that could be a horribly wrong assumption. Most of my 
development is done with RubyMotion, where this solution works. Your mileage 
may vary, especially if you are doing Objective-C/Swift development directly in 
Xcode.
