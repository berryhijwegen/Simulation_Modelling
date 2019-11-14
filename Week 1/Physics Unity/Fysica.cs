using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fysica : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
    public Vector3 startForce;
    public int mass;
    public int stretch;
    public int gravity;

    void FixedUpdate()
    {
        Force = -stretch * transform.position + -gravity * Velocity;
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
