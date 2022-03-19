#! /usr/bin/env python
import sys

from numpy import broadcast
import rospy
import geometry_msgs.msg
import tf
import tf2_ros

if __name__ == '__main__':
    if len(sys.argv) < 8:
        rospy.logerr('Invalid number of parameters \nusage: '
                    './static_turtle_tf3_broadcaster.py ' 'child_frame_name x y z roll pitch yaw')

        sys.exit(0)

    else:
        if sys.argv[0] == "world":
            rospy.logerr("Your static turtle name cannot be 'World'")
            sys.exit(0)

    rospy.init_node("my_static_tf2_broadcaster")
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    static_transform_stamped = geometry_msgs.msg.TransformStamped()

    static_transform_stamped.header.stamp = rospy.Time.now()
    static_transform_stamped.header.frame_id = "world"
    static_transform_stamped.child_frame_id = sys.argv[1]

    static_transform_stamped.transform.translation.x = float(sys.argv[2])
    static_transform_stamped.transform.translation.y = float(sys.argv[3])
    static_transform_stamped.transform.translation.z = float(sys.argv[4])

    quat = tf.transformations.quaternion_from_euler(float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))

    static_transform_stamped.transform.rotation.x = quat[0]
    static_transform_stamped.transform.rotation.y = quat[1]
    static_transform_stamped.transform.rotation.z = quat[2]
    static_transform_stamped.transform.rotation.w = quat[3]

    broadcaster.sendTransform(static_transform_stamped)
    rospy.spin()


