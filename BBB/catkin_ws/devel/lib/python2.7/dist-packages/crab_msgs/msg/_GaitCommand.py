"""autogenerated by genpy from crab_msgs/GaitCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GaitCommand(genpy.Message):
  _md5sum = "47aecd62b438a8407fd0203311383fc4"
  _type = "crab_msgs/GaitCommand"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 cmd
float64 fi
float64 velocity
float64 alpha
float64 scale

int32 RUNRIPPLE=1
int32 RUNTRIPOD=2
int32 STOP=3
int32 PAUSE=4

"""
  # Pseudo-constants
  RUNRIPPLE = 1
  RUNTRIPOD = 2
  STOP = 3
  PAUSE = 4

  __slots__ = ['cmd','fi','velocity','alpha','scale']
  _slot_types = ['int32','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cmd,fi,velocity,alpha,scale

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GaitCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.cmd is None:
        self.cmd = 0
      if self.fi is None:
        self.fi = 0.
      if self.velocity is None:
        self.velocity = 0.
      if self.alpha is None:
        self.alpha = 0.
      if self.scale is None:
        self.scale = 0.
    else:
      self.cmd = 0
      self.fi = 0.
      self.velocity = 0.
      self.alpha = 0.
      self.scale = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_i4d.pack(_x.cmd, _x.fi, _x.velocity, _x.alpha, _x.scale))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 36
      (_x.cmd, _x.fi, _x.velocity, _x.alpha, _x.scale,) = _struct_i4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_i4d.pack(_x.cmd, _x.fi, _x.velocity, _x.alpha, _x.scale))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 36
      (_x.cmd, _x.fi, _x.velocity, _x.alpha, _x.scale,) = _struct_i4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i4d = struct.Struct("<i4d")
