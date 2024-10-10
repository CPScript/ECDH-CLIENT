-- src/crypto.hs
module Crypto where

import Crypto.Error (CryptoFailable)
import Crypto.Number.Serialize (os2ip, ip2os)
import Crypto.PubKey.ECC (Curve, getCurveByName, generateKeyPair)
import Crypto.PubKey.ECC.Types (Point, getPointX, getPointY)
import Data.ByteArray (ByteArrayAccess, convert)
import Data.ByteString (ByteString)
import Data.ByteString.Char8 (pack, unpack)
import Data.String (fromString)
import Crypto.Hash (hashWith, SHA256)
import Crypto.Cipher.AES (AES256, encrypt, decrypt)
import Data.ByteString.Base64 (encode, decode)

-- Generate a key pair
generateKeyPair :: IO (Point, Point)
generateKeyPair = generateKeyPair curve

-- Define the curve
curve :: Curve
curve = getCurveByName "secp256k1"

-- ECDH key exchange
ecdhKeyExchange :: Point -> Point -> IO ByteString
ecdhKeyExchange publicKey privateKey = do
  let sharedSecret = multiply curve privateKey publicKey
  return $ serializePoint sharedSecret

-- Serialize a point
serializePoint :: Point -> ByteString
serializePoint point = os2ip $ getPointX point

-- Deserialize a point
deserializePoint :: ByteString -> Point
deserializePoint bytes = pointFromX curve $ ip2os bytes

-- Multiply two points
multiply :: Curve -> Point -> Point -> Point
multiply curve point1 point2 = pointMultiply curve point1 point2

-- Hash a message
hashMessage :: ByteString -> ByteString
hashMessage message = hashWith SHA256 message

-- Encrypt a message
encryptMessage :: ByteString -> ByteString -> ByteString
encryptMessage key message = encrypt AES256 key message

-- Decrypt a message
decryptMessage :: ByteString -> ByteString -> ByteString
decryptMessage key message = decrypt AES256 key message

-- Convert a string to a ByteString
stringToByteString :: String -> ByteString
stringToByteString string = pack string

-- Convert a ByteString to a string
byteStringToString :: ByteString -> String
byteStringToString bytes = unpack bytes
