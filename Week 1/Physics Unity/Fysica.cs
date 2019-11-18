using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fysica : MonoBehaviour
{
    public GameObject Origin;       // Origin object can be defined in Unity, object with script applied will use given object as origin
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;        // Set y value for spring movement, change x-asis value for rotation
    public int Mass;                // Set to 1 for spring movement/rotation
    public int Stretch;             // Set to 10 for spring movement/rotation
    public int Gravity;             // Set to 1 for spring movement, 0 for rotation

    void FixedUpdate()
    {
        Force = -Stretch * (transform.position - Origin.transform.position) + -Gravity * Velocity;
        Acceleration = Force / Mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
