from tf.transformations import euler_from_quaternion
from gazebo_msgs.srv import GetModelState
import rospy

def get_orientation():
    rospy.wait_for_service('/gazebo/get_model_state')
    try:
        get_model_state = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        response = get_model_state('drone', '')  # Replace 'drone' with the name of your drone model in Gazebo

        #  Quaternion to Euler angles will be converted here
        quaternion = response.pose.orientation
        euler = euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])

        roll, pitch, yaw = euler
        print(f'Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}')

    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == '__main__':
    rospy.init_node('get_orientation')
    get_orientation()
