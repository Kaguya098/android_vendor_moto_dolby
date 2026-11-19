# Dolby (TranOS16) vendor module
# Pemakaian di device.mk:  $(call inherit-product, vendor/infinix/Dolby/config.mk)

DOLBY_PATH := vendor/infinix/Dolby
DOLBY_BLOB := $(DOLBY_PATH)/proprietary/vendor

PRODUCT_SOONG_NAMESPACES += $(DOLBY_PATH)

PRODUCT_PACKAGES += \
    libdapparamstorage \
    libdeccfg \
    libdlbpreg \
    libstagefrightdolby \
    libstagefright_soft_ac4dec \
    libstagefright_soft_ddpdec \
    vendor.dolby.hardware.dms@2.0 \
    libdlbvol \
    libswdap \
    libswgamedap \
    libswvqe \
    libdlbdsservice \
    vendor.dolby.hardware.dms@2.0-impl \
    libstagefright_foundation_dolby \
    libsqlite_dolby \
    vendor.dolby.hardware.dms@2.0-service \
    LunarisDolby

PRODUCT_COPY_FILES += \
    $(DOLBY_BLOB)/etc/dolby/dax-default.xml:$(TARGET_COPY_OUT_VENDOR)/etc/dolby/dax-default.xml \
    $(DOLBY_BLOB)/etc/media_codecs_dolby_audio.xml:$(TARGET_COPY_OUT_VENDOR)/etc/media_codecs_dolby_audio.xml


BOARD_VENDOR_SEPOLICY_DIRS += $(DOLBY_PATH)/sepolicy/vendor
